#!/usr/bin/env python
import ROOT as rt
from decimal import Decimanl
def round20(err):

    errStr = str(err)
    errList = list(errStr)
    dotIndex = errList.index('.')
    errList.pop(dotIndex)

    eStr = ''
    if 'e' in errStr:
        eIndex = errList.index('e')
        eStr = ''.join(errList[eIndex:])
        errList = errList[:eIndex] 
    for i in xrange(len(errList)):
        if int(''.join(errList[:i+1])) < 20:
            tmpList = errList[:i+1]
            errLastDig = int(errList[i+1])
        else:
            if errLastDig >= 5:
                tmpList[-1] = str(int(tmpList[-1])+1)
            if len(tmpList) < dotIndex + 1:
                toAdd = (dotIndex+1) - len(tmpList)
                tmpList.extend('0'*toAdd)
            tmpList.insert(dotIndex,'.')
    
            finNum = rt.Double(''.join(tmpList)+eStr)
            return finNum


def roundOffErr(value, err):

    newErr = round20(err)
    valStr = str(value)
    errStr = str(newErr)

    if '.' not in valStr and 'e' not in valStr:
        valStr += '.0'

    if '.' not in errStr and 'e' not in errStr:
        errStr += '.0'

    valList = list(valStr)
    errList = list(errStr)

    if 'e' in valStr:
        valIndex = valList.index('e')
        valExp = int(''.join(valList[valIndex+1:]))
        valList = list(valStr.split('e')[0])

        if valExp < 0:
            valList = [0,'.'] + [0] * (abs(valExp)-1) + valList

        else:
            valList = valList + [0] * abs(valExp) + ['.',0]

    if 'e' in errStr:
        errIndex = errList.index('e')
        errExp = int(''.join(errList[errIndex+1:]))
        errList = list(errStr.split('e')[0])

        if errExp < 0:
            errList = [0,'.'] + [0] * (abs(errExp)-1) + errList

        else:
            errList = errList + [0] * abs(errExp) + ['.',0]

    valDotIndex = valList.index('.')
    errDotIndex = errList.index('.')

    valListLeft = valList[:valDotIndex]
    valListRight = valList[valDotIndex+1:]
    errListLeft = errList[:errDotIndex]
    errListRight = errList[errDotIndex+1:]

    if newErr < 1:
        if len(valListRight) < len(errListRight):
            valErrDiff = len(errListRight)-len(valListRight)
            valListRight + ['0']*(valErrDiff+1)
            valListRight = valListRight[:len(errListRight)]

        elif len(valListRight) > len(errListRight):
            errLenRight = len(errListRight)
            print errLenRight
            print valListRight[errLenRight]
            valLastDig = valListRight[errLenRight]
            valListRight = valListRight[:errLenRight]

            if int(valLastDig) >= 5:
                valListRight[-1] = str(int(valListRight[-1])+1)

        elif len(valListRight) == len(errListRight):
            valListRight = valListRight

    elif newErr > 1:
        j = 0

        for i in reversed(range(len(errListLeft))):
            if errListLeft[i] == '0':
                j += 1
                continue

            roundIndex = -i
            break
       
        if len(errListLeft) <= 2:
            valLastDig = int(valListRight[0])

        else:
            valLastDig = int(valListLeft[roundIndex+1])

        if roundIndex == -1:
            valListLeft = valListLeft[:len(valListLeft)]

        else:
            valListLeft = valListLeft[:roundIndex+1]

        valListLeft.extend('0' * j)

        if valLastDig >= 5:
            valListLeft[roundIndex] = str(int(valListLeft[roundIndex])+1)

        valListRight = ['0']

    valStrFin = ''.join(valListLeft)+'.'+''.join(valListRight)
    valueFin = rt.Double(valStrFin)

    return valueFin, newErr
        

    
if __name__ == "__main__":
    print '12345.111 0.00232'
    print roundOffErr(12345.111, 0.00232)

    print '12345.221 13.56'
    print roundOffErr(12345.221, 13.56)

    print '12345.11122353 0.000003632'
    print roundOffErr('12345.11122353', '0.000003632')
