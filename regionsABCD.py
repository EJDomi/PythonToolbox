#!/usr/bin/env python 
import ROOT as rt
from anaTp import *
from ABCDRegions_cfi import *
from math import *
from round20 import *
def TradRound(num):
    return round(num+10**(-len(str(num))-1),2)
doData = False
def makeTables(RegionA, RegionB, RegionC, RegionD, outFileName, doubleRatioFile, syst=0.1):
     
    cutANum = {}
    cutBNum = {}
    cutCNum = {}
    cutDNum = {}
    cutANum['MC_Background'] = rt.Double(0)
    cutBNum['MC_Background'] = rt.Double(0)
    cutCNum['MC_Background'] = rt.Double(0)
    cutDNum['MC_Background'] = rt.Double(0)
    cutDNum['EstBackground'] = rt.Double(0)
    cutANum['Other'] = rt.Double(0)
    cutBNum['Other'] = rt.Double(0)
    cutCNum['Other'] = rt.Double(0)
    cutDNum['Other'] = rt.Double(0)

    cutANumErr = {}
    cutBNumErr = {}
    cutCNumErr = {}
    cutDNumErr = {}
    cutANumErr['MC_Background'] = rt.Double(0)
    cutBNumErr['MC_Background'] = rt.Double(0)
    cutCNumErr['MC_Background'] = rt.Double(0)
    cutDNumErr['MC_Background'] = rt.Double(0)
    cutDNumErr['EstBackground'] = rt.Double(0)
    cutANumErr['Other'] = rt.Double(0)
    cutBNumErr['Other'] = rt.Double(0)
    cutCNumErr['Other'] = rt.Double(0)
    cutDNumErr['Other'] = rt.Double(0)
    cutAErrSum = rt.Double(0)
    cutBErrSum = rt.Double(0)
    cutCErrSum = rt.Double(0)
    cutDErrSum = rt.Double(0)
    cutDSum = rt.Double(0)
    cutAOtherErrSum = rt.Double(0)
    cutBOtherErrSum = rt.Double(0)
    cutCOtherErrSum = rt.Double(0)
    cutDOtherErrSum = rt.Double(0)
    ratios = {}
    ratios['MC'] = {}
    ratios['dataQCD'] = {}
    ratios['Data'] = {}
    ratiosErr = {}
    ratiosErr['MC'] = {} 
    ratiosErr['dataQCD'] = {}
    ratiosErr['Data'] = {}
    for var in RegionA:
        for hist in RegionA[var]:
            if 'tH' in hist:
                tH = True
                tZ = False
            elif 'tZ' in hist:
                tH = False
                tZ = True
            cutANum[hist] = rt.Double(0)
            cutANumErr[hist] = rt.Double(0)
            cutANum[hist] = RegionA[var][hist].IntegralAndError(1,1000,cutANumErr[hist])
            if 'TTJets' in hist:
                cutANumErr[hist] = rt.TMath.Sqrt(cutANumErr[hist]**2 + (syst * cutANum[hist])**2)
            if 'data' in hist or 'Data' in hist or 'est' in hist or 'LH' in hist or 'RH' in hist or 'QCD' in hist or ('TpTp' in hist):
                continue
            if 'TTJets' not in hist:
                cutANum['Other'] += cutANum[hist]
                cutAOtherErrSum += cutANumErr[hist]*cutANumErr[hist]
            cutANum['MC_Background'] += cutANum[hist]
            cutAErrSum += cutANumErr[hist]*cutANumErr[hist]
    for var in RegionB:
        for hist in RegionB[var]:
            cutBNum[hist] = rt.Double(0)
            cutBNumErr[hist] = rt.Double(0)
            cutBNum[hist] = RegionB[var][hist].IntegralAndError(1,1000,cutBNumErr[hist])
            if 'TTJets' in hist:
                cutBNumErr[hist] = rt.TMath.Sqrt(cutBNumErr[hist]**2 + (syst * cutBNum[hist])**2)
            if 'data' in hist or 'Data' in hist or 'est' in hist or 'LH' in hist or 'RH' in hist or 'QCD' in hist or ('TpTp' in hist):
                continue
            if 'TTJets' not in hist:
                cutBNum['Other'] += cutBNum[hist]
                cutBOtherErrSum += cutBNumErr[hist]*cutBNumErr[hist]
            cutBNum['MC_Background'] += cutBNum[hist]
            cutBErrSum += cutBNumErr[hist]*cutBNumErr[hist]
    for var in RegionC:
        for hist in RegionC[var]:
            cutCNum[hist] = rt.Double(0)
            cutCNumErr[hist] = rt.Double(0)
            cutCNum[hist] = RegionC[var][hist].IntegralAndError(1,1000,cutCNumErr[hist])
            if 'TTJets' in hist:
                cutCNumErr[hist] = rt.TMath.Sqrt(cutCNumErr[hist]**2 + (syst * cutCNum[hist])**2)
            if 'data' in hist or 'Data' in hist or 'est' in hist or 'LH' in hist or 'RH' in hist or 'QCD' in hist or ('TpTp' in hist):
                continue
            if 'TTJets' not in hist:
                cutCNum['Other'] += cutCNum[hist]
                cutCOtherErrSum += cutCNumErr[hist]*cutCNumErr[hist]
            cutCNum['MC_Background'] += cutCNum[hist]
            cutCErrSum += cutCNumErr[hist]*cutCNumErr[hist]
    for var in RegionD:
        for hist in RegionD[var]:
            cutDNum[hist] = rt.Double(0)
            cutDNumErr[hist] = rt.Double(0)
            cutDNum[hist] = RegionD[var][hist].IntegralAndError(1,1000,cutDNumErr[hist])
            if 'TTJets' in hist:
                cutDNumErr[hist] = rt.TMath.Sqrt(cutDNumErr[hist]**2 + (syst * cutDNum[hist])**2)
            if 'data' in hist or 'Data' in hist or 'est' in hist or 'LH' in hist or 'RH' in hist or 'QCD' in hist or ('TpTp' in hist):
                continue
            if 'TTJets' not in hist:
                cutDNum['Other'] += cutDNum[hist]
                cutDOtherErrSum += cutDNumErr[hist]*cutDNumErr[hist]
            cutDNum['MC_Background'] += cutDNum[hist]
            cutDErrSum += cutDNumErr[hist]*cutDNumErr[hist]
            cutDSum += cutDNum[hist]
   
    cutANumErr['dataQCD'] = rt.TMath.Sqrt(cutANum['Data']+cutAErrSum) 
    cutBNumErr['dataQCD'] = rt.TMath.Sqrt(cutBNum['Data']+cutBErrSum) 
    cutCNumErr['dataQCD'] = rt.TMath.Sqrt(cutCNum['Data']+cutCErrSum) 
    print cutANum['dataQCD'], cutBNum['dataQCD'], cutCNum['dataQCD']
    cutDNumErr['estQCD'] = cutDNum['estQCD']*rt.TMath.Sqrt((cutANumErr['dataQCD']/cutANum['dataQCD'])**2+(cutBNumErr['dataQCD']/cutBNum['dataQCD'])**2+(cutCNumErr['dataQCD']/cutCNum['dataQCD'])**2) 

    cutANum['MC_Background'] += cutANum['QCD']
    cutBNum['MC_Background'] += cutBNum['QCD']
    cutCNum['MC_Background'] += cutCNum['QCD']
    cutDNum['MC_Background'] += cutDNum['QCD']

    cutANumErr['MC_Background'] = rt.TMath.Sqrt(cutANumErr['QCD']*cutANumErr['QCD']+cutAErrSum)
    cutBNumErr['MC_Background'] = rt.TMath.Sqrt(cutBNumErr['QCD']*cutBNumErr['QCD']+cutBErrSum)
    cutCNumErr['MC_Background'] = rt.TMath.Sqrt(cutCNumErr['QCD']*cutCNumErr['QCD']+cutCErrSum)
    cutDNumErr['MC_Background'] = rt.TMath.Sqrt(cutDNumErr['QCD']*cutDNumErr['QCD']+cutDErrSum)

    cutANumErr['Other'] = rt.TMath.Sqrt(cutAOtherErrSum) 
    cutBNumErr['Other'] = rt.TMath.Sqrt(cutBOtherErrSum) 
    cutCNumErr['Other'] = rt.TMath.Sqrt(cutCOtherErrSum) 
    cutDNumErr['Other'] = rt.TMath.Sqrt(cutDOtherErrSum) 
    
    cutDNum['EstBackground'] = cutDNum['estQCD'] + cutDSum
    cutDNumErr['EstBackground'] = rt.TMath.Sqrt(cutDNumErr['estQCD']*cutDNumErr['estQCD']+ cutDErrSum)


    for num in cutANum:
        if 'QCD' in num and 'est' not in num and 'data' not in num:
            if cutANum[num] == 0: continue
            if cutBNum[num] == 0: continue
            if cutCNum[num] == 0: continue
            if cutDNum[num] == 0: continue
            ratios['MC']['A/C'] = cutANum[num] / cutCNum[num]        
            ratios['MC']['A/B'] = cutANum[num] / cutBNum[num]        
            ratios['MC']['B/D'] = cutBNum[num] / cutDNum[num]
            ratios['MC']['C/D'] = cutCNum[num] / cutDNum[num]
            ratiosErr['MC']['A/C'] = ratios['MC']['A/C']*rt.TMath.Sqrt((cutANumErr[num]/cutANum[num])**2+(cutCNumErr[num]/cutCNum[num])**2)        
            ratiosErr['MC']['A/B'] = ratios['MC']['A/B']*rt.TMath.Sqrt((cutANumErr[num]/cutANum[num])**2+(cutBNumErr[num]/cutBNum[num])**2)
            ratiosErr['MC']['B/D'] = ratios['MC']['B/D']*rt.TMath.Sqrt((cutBNumErr[num]/cutBNum[num])**2+(cutDNumErr[num]/cutDNum[num])**2)
            ratiosErr['MC']['C/D'] = ratios['MC']['C/D']*rt.TMath.Sqrt((cutCNumErr[num]/cutCNum[num])**2+(cutDNumErr[num]/cutDNum[num])**2)

            ratios['MC']['(A/C)/(B/D)'] = ratios['MC']['A/C'] / ratios['MC']['B/D']
            ratios['MC']['(A/B)/(C/D)'] = ratios['MC']['A/B'] / ratios['MC']['C/D']
            ratiosErr['MC']['(A/C)/(B/D)'] = ratios['MC']['(A/C)/(B/D)'] * rt.TMath.Sqrt((ratiosErr['MC']['A/C']/ratios['MC']['A/C'])**2 + (ratiosErr['MC']['B/D']/ratios['MC']['B/D'])**2)
            ratiosErr['MC']['(A/B)/(C/D)'] = ratios['MC']['(A/B)/(C/D)'] * rt.TMath.Sqrt((ratiosErr['MC']['A/B']/ratios['MC']['A/B'])**2 + (ratiosErr['MC']['C/D']/ratios['MC']['C/D'])**2)
            with open(doubleRatioFile,'a') as doub:
                doub.write('\'MCQCD\' : { \n')
                doub.write('\'value\' : ' + str(ratios['MC']['(A/C)/(B/D)']) + '\n')
                doub.write('\'error\' : ' + str(ratiosErr['MC']['(A/C)/(B/D)']) + '}\n')
                doub.close()

        elif 'data' in num:
            if cutANum[num] == 0: continue
            if cutBNum[num] == 0: continue
            if cutCNum[num] == 0: continue
            if cutDNum[num] == 0: continue
            ratios[num]['A/C'] = cutANum[num] / cutCNum[num]        
            ratios[num]['A/B'] = cutANum[num] / cutBNum[num]
            ratios[num]['B/D'] = cutBNum[num] / cutDNum[num]
            ratios[num]['C/D'] = cutCNum[num] / cutDNum[num]
            ratiosErr[num]['A/C'] = ratios[num]['A/C']*rt.TMath.Sqrt((cutANumErr[num]/cutANum[num])**2+(cutCNumErr[num]/cutCNum[num])**2)        
            ratiosErr[num]['A/B'] = ratios[num]['A/B']*rt.TMath.Sqrt((cutANumErr[num]/cutANum[num])**2+(cutBNumErr[num]/cutBNum[num])**2)
            ratiosErr[num]['B/D'] = ratios[num]['B/D']*rt.TMath.Sqrt((cutBNumErr[num]/cutBNum[num])**2+(cutDNumErr[num]/cutDNum[num])**2)
            ratiosErr[num]['C/D'] = ratios[num]['C/D']*rt.TMath.Sqrt((cutCNumErr[num]/cutCNum[num])**2+(cutDNumErr[num]/cutDNum[num])**2)
            ratios[num]['(A/C)/(B/D)'] = ratios[num]['A/C'] / ratios[num]['B/D']
            ratios[num]['(A/B)/(C/D)'] = ratios[num]['A/B'] / ratios[num]['C/D']
            ratiosErr[num]['(A/C)/(B/D)'] = ratios[num]['(A/C)/(B/D)'] * rt.TMath.Sqrt((ratiosErr[num]['A/C']/ratios[num]['A/C'])**2 + (ratiosErr[num]['B/D']/ratios[num]['B/D'])**2)
            ratiosErr[num]['(A/B)/(C/D)'] = ratios[num]['(A/B)/(C/D)'] * rt.TMath.Sqrt((ratiosErr[num]['A/B']/ratios[num]['A/B'])**2 + (ratiosErr[num]['C/D']/ratios[num]['C/D'])**2)
        elif 'Data' in num:    
            ratios[num]['A/C'] = cutANum[num] / cutCNum[num]        
            ratios[num]['A/B'] = cutANum[num] / cutBNum[num]
            ratiosErr[num]['A/C'] = ratios[num]['A/C']*rt.TMath.Sqrt((rt.TMath.Sqrt(cutANum[num])/cutANum[num])**2+(rt.TMath.Sqrt(cutCNum[num])/cutCNum[num])**2)        
            ratiosErr[num]['A/B'] = ratios[num]['A/B']*rt.TMath.Sqrt((rt.TMath.Sqrt(cutANum[num])/cutANum[num])**2+(rt.TMath.Sqrt(cutBNum[num])/cutBNum[num])**2)
        elif 'est' not in num and ('TTJets' in num or 'LH' in num or 'RH' in num):
            if cutANum[num] == 0: continue
            if cutBNum[num] == 0: continue
            if cutCNum[num] == 0: continue
            if cutDNum[num] == 0: continue
            ratios[num] = {}
            ratiosErr[num] = {}
            ratios[num]['A/C'] = cutANum[num] / cutCNum[num]        
            ratios[num]['A/B'] = cutANum[num] / cutBNum[num]        
            ratios[num]['B/D'] = cutBNum[num] / cutDNum[num]
            ratios[num]['C/D'] = cutCNum[num] / cutDNum[num]
            ratiosErr[num]['A/C'] = ratios[num]['A/C']*rt.TMath.Sqrt((cutANumErr[num]/cutANum[num])**2+(cutCNumErr[num]/cutCNum[num])**2)        
            ratiosErr[num]['A/B'] = ratios[num]['A/B']*rt.TMath.Sqrt((cutANumErr[num]/cutANum[num])**2+(cutBNumErr[num]/cutBNum[num])**2)
            ratiosErr[num]['B/D'] = ratios[num]['B/D']*rt.TMath.Sqrt((cutBNumErr[num]/cutBNum[num])**2+(cutDNumErr[num]/cutDNum[num])**2)
            ratiosErr[num]['C/D'] = ratios[num]['C/D']*rt.TMath.Sqrt((cutCNumErr[num]/cutCNum[num])**2+(cutDNumErr[num]/cutDNum[num])**2)

            ratios[num]['(A/C)/(B/D)'] = ratios[num]['A/C'] / ratios[num]['B/D']
            ratios[num]['(A/B)/(C/D)'] = ratios[num]['A/B'] / ratios[num]['C/D']
            ratiosErr[num]['(A/C)/(B/D)'] = ratios[num]['(A/C)/(B/D)'] * rt.TMath.Sqrt((ratiosErr[num]['A/C']/ratios[num]['A/C'])**2 + (ratiosErr[num]['B/D']/ratios[num]['B/D'])**2)
            ratiosErr[num]['(A/B)/(C/D)'] = ratios[num]['(A/B)/(C/D)'] * rt.TMath.Sqrt((ratiosErr[num]['A/B']/ratios[num]['A/B'])**2 + (ratiosErr[num]['C/D']/ratios[num]['C/D'])**2)
            with open(doubleRatioFile,'a') as doub:
                doub.write('\''+num+'\' : { \n')
                doub.write('\'value\' : ' + str(ratios[num]['(A/C)/(B/D)']) + '\n')
                doub.write('\'error\' : ' + str(ratiosErr[num]['(A/C)/(B/D)']) + '}\n')
                doub.close()
 
    with open(doubleRatioFile,'a') as doub:
        doub.write('}\n')
        doub.close()
    with open(outFileName,'w') as f:
        f.write('     hist              Region A                     Region B                     Region C                      Region D      \n')
        for key in sorted(cutANum):
            spacing = ' ' * (18-len(key))
            if 'Data' in key:
                f.write(' '+str(key)+spacing+str(TradRound(cutANum[key]))+' ' * (30-len(str(TradRound(cutANum[key]))))+str(TradRound(cutBNum[key]))+' ' * (30-len(str(TradRound(cutBNum[key]))))+str(TradRound(cutCNum[key]))+' ' * (30-len(str(TradRound(cutBNum[key]))))+str(TradRound(cutDNum[key]))+ ' \pm ' +str(TradRound(cutDNumErr[key]))+'\n')
                #f.write(' '+str(key)+spacing+str(TradRound(cutANum[key]))+' ' * (30-len(str(TradRound(cutANum[key]))))+str(TradRound(cutBNum[key]))+' ' * (30-len(str(TradRound(cutBNum[key]))))+str(TradRound(cutCNum[key]))+' ' * (30-len(str(TradRound(cutBNum[key]))))+'\n')
            elif 'data' in key:
                f.write(' '+str(key)+spacing+str(TradRound(cutANum[key]))+ ' \pm '+ str(TradRound(cutANumErr[key]))+' ' * (30-len(str(TradRound(cutANum[key]))+ ' \pm '+ str(TradRound(cutANumErr[key]))))+str(TradRound(cutBNum[key])) +' \pm '+ str(TradRound(cutBNumErr[key]))+' ' * (30-len(str(TradRound(cutBNum[key])) +' \pm '+ str(TradRound(cutBNumErr[key]))))+str(TradRound(cutCNum[key])) + ' \pm ' +str(TradRound(cutCNumErr[key]))+' ' * (30-len(str(TradRound(cutCNum[key])) + ' \pm ' +str(TradRound(cutCNumErr[key]))))+ ' '+str(TradRound(cutDNum[key]))+ ' \pm ' +str(TradRound(cutDNumErr[key]))+'\n')
                #f.write(' '+str(key)+spacing+str(TradRound(cutANum[key]))+ ' \pm '+ str(TradRound(cutANumErr[key]))+' ' * (30-len(str(TradRound(cutANum[key]))+ ' \pm '+ str(TradRound(cutANumErr[key]))))+str(TradRound(cutBNum[key])) +' \pm '+ str(TradRound(cutBNumErr[key]))+' ' * (30-len(str(TradRound(cutBNum[key])) +' \pm '+ str(TradRound(cutBNumErr[key]))))+str(TradRound(cutCNum[key])) + ' \pm ' +str(TradRound(cutCNumErr[key]))+' ' * (30-len(str(TradRound(cutCNum[key])) + ' \pm ' +str(TradRound(cutCNumErr[key]))))+'\n')
            else:
                f.write(' '+str(key)+spacing+str(TradRound(cutANum[key]))+ ' \pm '+ str(TradRound(cutANumErr[key]))+' ' * (30-len(str(TradRound(cutANum[key]))+ ' \pm '+ str(TradRound(cutANumErr[key]))))+str(TradRound(cutBNum[key])) +' \pm '+ str(TradRound(cutBNumErr[key]))+' ' * (30-len(str(TradRound(cutBNum[key])) +' \pm '+ str(TradRound(cutBNumErr[key]))))+str(TradRound(cutCNum[key])) + ' \pm ' +str(TradRound(cutCNumErr[key]))+' ' * (30-len(str(TradRound(cutCNum[key])) + ' \pm ' +str(TradRound(cutCNumErr[key]))))+str(TradRound(cutDNum[key]))+ ' \pm ' +str(TradRound(cutDNumErr[key]))+'\n')
        f.write(' '+'estQCD'+(' '*(18-len('estQCD')))+str(TradRound(cutDNum['estQCD']))+ ' \pm ' +str(TradRound(cutDNumErr['estQCD']))+'\n')
        f.write(' '+'estBackground'+(' '*(18-len('EstBackground')))+str(TradRound(cutDNum['EstBackground']))+ ' \pm ' +str(TradRound(cutDNumErr['EstBackground']))+'\n\n')

        for key in ratios:
            if 'QCD' in key or 'Data' in key or 'MC' in key:
                f.write(key+'\n')
                f.write('\nRaw value:\n')
                for ratio in ratios[key]:
                    f.write(' '+ratio+ ': ' + str(ratios[key][ratio]) + ' \pm ' + str((ratiosErr[key][ratio]))+ '\n') 
                #f.write('\nRounded value:\n')
                #for ratio in ratios[key]:
                #    ratioRounded, ratioRoundedErr = roundOffErr(ratios[key][ratio], ratiosErr[key][ratio])
                #    f.write(' '+ratio+ ': ' + str(ratioRounded) + ' \pm ' + str((ratioRoundedErr)) + '\n')
        f.close()
    return cutDNumErr['estQCD']

if __name__ == "__main__":

    cutA,cutB,cutC,cutD =  ABCD(RegionA,RegionB,RegionC,RegionD,False)
    makeTables(cutA, cutB, cutC, cutD, 'eventsABCD_CHS.txt')
