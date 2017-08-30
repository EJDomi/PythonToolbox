#!/usr/bin/env python 

from anaTp import *
import re
pre = analysis(Cutflow_pre, 'Nominal', 'Wts', 'SigWts', output = False)
higgs = analysis(Cutflow_higgs, 'Nominal', 'Wts', 'SigWts', output = False)
top = analysis(Cutflow_top, 'Nominal', 'Wts', 'SigWts', output = False)
end = analysis(Cutflow_higgs_top, 'Nominal', 'Wts', 'SigWts', output = False)

preNum = {}
higgsNum = {}
topNum = {}
endNum = {}

for hist in pre['ht']:
    preNum[hist] = pre['ht'][hist].Integral(0,1000)/lumi
for hist in higgs['ht']:
    higgsNum[hist] = higgs['ht'][hist].Integral(0,1000)/lumi
for hist in top['ht']:
    topNum[hist] = top['ht'][hist].Integral(0,1000)/lumi
for hist in end['ht']:
    endNum[hist] = end['ht'][hist].Integral(0,1000)/lumi



with open('efficiencies_17Aug17.txt','w') as f:
    f.write('|   sample   |   presel   |   H tag   |    t tag    |   t Tag + H tag   |\n')
    for key in preNum:
        if 'LH' in key or 'RH' in key:
            f.write(' '+str(key)+'   '+str(preNum[key])+'   '+str(higgsNum[key])+'   '+str(topNum[key])+'   '+str(endNum[key])+'\n')
