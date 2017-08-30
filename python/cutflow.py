#!/usr/bin/env python 
import ROOT as rt
from anaTp import *
import re
def TradRound(num):
    return round(num+10**(-len(str(num))-1),2)
pre = analysis(Cutflow_pre, 'Nominal', 'Wts', 'SigWts', output = False)
higgs = analysis(Cutflow_higgs, 'Nominal', 'Wts', 'SigWts', output = False)
top = analysis(Cutflow_top, 'Nominal', 'Wts', 'SigWts', output = False)
end = analysis(Cutflow_higgs_top, 'Nominal', 'Wts', 'SigWts', output = False)

preNum = {}
higgsNum = {}
topNum = {}
endNum = {}

preNumErr = {}
higgsNumErr = {}
topNumErr = {}
endNumErr = {}
for hist in end['ht']:
    preNumErr[hist] = rt.Double(0)
    higgsNumErr[hist] = rt.Double(0)
    topNumErr[hist] = rt.Double(0)
    endNumErr[hist] = rt.Double(0)
for hist in pre['ht']:
    preNum[hist] = pre['ht'][hist].IntegralAndError(0,1000,preNumErr[hist])
for hist in higgs['ht']:
    higgsNum[hist] = top['ht'][hist].IntegralAndError(0,1000,higgsNumErr[hist])
for hist in top['ht']:
    topNum[hist] = top['ht'][hist].IntegralAndError(0,1000,topNumErr[hist])
for hist in end['ht']:
    endNum[hist] = end['ht'][hist].IntegralAndError(0,1000,endNumErr[hist])

preNum['Background'] = rt.Double(0)
higgsNum['Background'] = rt.Double(0)
topNum['Background'] = rt.Double(0)
endNum['Background'] = rt.Double(0)
preNumErr['Background'] = rt.Double(0)
higgsNumErr['Background'] = rt.Double(0)
topNumErr['Background'] = rt.Double(0)
endNumErr['Background'] = rt.Double(0)

preErrSum = rt.Double(0)
higgsErrSum = rt.Double(0)
topErrSum = rt.Double(0)
endErrSum = rt.Double(0)

for hist in end['ht']:
    if 'Tbt' in hist or 'Ttt' in hist or 'Data' in hist:
        continue
    preNum['Background'] += preNum[hist]
    higgsNum['Background'] += higgsNum[hist]
    topNum['Background'] += topNum[hist]
    endNum['Background'] += endNum[hist]
    preErrSum += preNum[hist]*preNum[hist]
    higgsErrSum += higgsNum[hist]*higgsNum[hist]
    topErrSum += topNum[hist]*topNum[hist]
    endErrSum += endNum[hist]*endNum[hist]

preNumErr['Background'] = rt.TMath.Sqrt(preErrSum)
higgsNumErr['Background'] = rt.TMath.Sqrt(higgsErrSum)
topNumErr['Background'] = rt.TMath.Sqrt(topErrSum)
endNumErr['Background'] = rt.TMath.Sqrt(endErrSum)

with open('eventsCutflow_27Aug17.txt','w') as f:
    f.write('|      sample      |      presel      |      H tag      |      t tag      |      t Tag + H tag      |\n')
    for key in endNum:
        if 'data' in key or 'Data' in key:
            f.write(' '+str(key)+'   '+str(TradRound(preNum[key]))+' \pm '+str(TradRound(preNumErr[key]))+'   '+str(TradRound(higgsNum[key]))+' \pm '+str(TradRound(higgsNumErr[key]))+'   '+str(TradRound(topNum[key]))+' \pm '+str(TradRound(topNumErr[key]))+'\n')
        else:
            f.write(' '+str(key)+'   '+str(TradRound(preNum[key]))+' \pm '+str(TradRound(preNumErr[key]))+'   '+str(TradRound(higgsNum[key]))+' \pm '+str(TradRound(higgsNumErr[key]))+'   '+str(TradRound(topNum[key]))+' \pm '+str(TradRound(topNumErr[key]))+'   '+str(TradRound(endNum[key]))+' \pm '+str(TradRound(endNumErr[key]))+'\n')

