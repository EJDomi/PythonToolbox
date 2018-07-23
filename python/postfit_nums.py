#!/usr/bin/env python

import ROOT as rt
from collections import OrderedDict

def TradRound(num):
    return round(num+10**(-len(str(num))-1),1)


histNameTemps = OrderedDict([
('QCD', [ 'tH_RA', 'tH_RB', 'tH_RC', 'tH_RD', 'tZ_RA', 'tZ_RB', 'tZ_RC', 'tZ_RD' ]),
('TTJets', [ 'tH_RA', 'tH_RB', 'tH_RC', 'tH_RD', 'tZ_RA', 'tZ_RB', 'tZ_RC', 'tZ_RD' ]),
('Other', [ 'tH_RA', 'tH_RB', 'tH_RC', 'tH_RD', 'tZ_RA', 'tZ_RB', 'tZ_RC', 'tZ_RD' ]),
('TotalBkg', [ 'tH_RA', 'tH_RB', 'tH_RC', 'tH_RD', 'tZ_RA', 'tZ_RB', 'tZ_RC', 'tZ_RD' ]),
('data_obs', [ 'tH_RA', 'tH_RB', 'tH_RC', 'tH_RD', 'tZ_RA', 'tZ_RB', 'tZ_RC', 'tZ_RD' ]),
])

def getTable(iFile, oFile):

    f = rt.TFile.Open(iFile, 'r')

    hists = {}
    
    with open(oFile+'_tH.txt', 'w') as ofH:
        with open(oFile+'_tZ.txt', 'w') as ofZ:
            ofH.write('{:18} & {:^18} & {:^18} & {:^18} & {:^18} \\\\\n'.format('', 'A', 'B', 'C', 'D'))
            ofZ.write('{:18} & {:^18} & {:^18} & {:^18} & {:^18} \\\\\n'.format('', 'W', 'X', 'Y', 'Z'))

            for name in histNameTemps:
                print 
                histA = f.Get(histNameTemps[name][0]+'_postfit/'+name)
                histB = f.Get(histNameTemps[name][1]+'_postfit/'+name)
                histC = f.Get(histNameTemps[name][2]+'_postfit/'+name)
                histD = f.Get(histNameTemps[name][3]+'_postfit/'+name)
                histW = f.Get(histNameTemps[name][4]+'_postfit/'+name)
                histX = f.Get(histNameTemps[name][5]+'_postfit/'+name)
                histY = f.Get(histNameTemps[name][6]+'_postfit/'+name)
                histZ = f.Get(histNameTemps[name][7]+'_postfit/'+name)
                
                errA = rt.Double(0)
                errB = rt.Double(0)
                errC = rt.Double(0)
                errD = rt.Double(0)
                errW = rt.Double(0)
                errX = rt.Double(0)
                errY = rt.Double(0)
                errZ = rt.Double(0)
                numA = histA.IntegralAndError(1,1000,errA)
                numB = histB.IntegralAndError(1,1000,errB)
                numC = histC.IntegralAndError(1,1000,errC)
                numD = histD.IntegralAndError(1,1000,errD)
                numW = histW.IntegralAndError(1,1000,errW)
                numX = histX.IntegralAndError(1,1000,errX)
                numY = histY.IntegralAndError(1,1000,errY)
                numZ = histZ.IntegralAndError(1,1000,errZ)

                ofH.write('{:<18} & ${:>6} \pm {:<5}$ & ${:>6} \pm {:<5}$ & ${:>6} \pm {:<5}$ & ${:>6} \pm {:<5}$ \\\\\n'.format(name, TradRound(numA), TradRound(errA), 
                                                                                                                                       TradRound(numB), TradRound(errB), 
                                                                                                                                       TradRound(numC), TradRound(errC), 
                                                                                                                                       TradRound(numD), TradRound(errD))) 
                ofZ.write('{:<18} & ${:>6} \pm {:<5}$ & ${:>6} \pm {:<5}$ & ${:>6} \pm {:<5}$ & ${:>6} \pm {:<5}$ \\\\\n'.format(name, TradRound(numW), TradRound(errW), 
                                                                                                                                       TradRound(numX), TradRound(errX), 
                                                                                                                                       TradRound(numY), TradRound(errY), 
                                                                                                                                       TradRound(numZ), TradRound(errZ)))

if  __name__ == "__main__":
    getTable('./postfitshapes.root', 'postfit_26Jun18') 
