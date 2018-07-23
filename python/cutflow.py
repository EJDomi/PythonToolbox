#!/usr/bin/env python 
import ROOT as rt
from anaTp import *
import re
from variableDictionaries_cfi import *
from round20 import *
def TradRound(num):
    return round(num+10**(-len(str(num))-1),2)

jetType = 'CHS'
QCDType = 'Pt'
pre = analysis(Cutflow_pre, 'Nominal', 'Wts', 'SigWts', False, './dontMatterPre', jetType, QCDType)
init = analysis(Cutflow_init, 'Nominal', 'Wts', 'SigWts', False, './dontMatterHiggs', jetType, QCDType)
extra = analysis(Cutflow_extra, 'Nominal', 'Wts', 'SigWts', False, './dontMatterTop', jetType, QCDType)
forward = analysis(Cutflow_forward, 'Nominal', 'Wts', 'SigWts', False, './dontMatterTop', jetType, QCDType)
annulus = analysis(Cutflow_annulus, 'Nominal', 'Wts', 'SigWts', False, './dontMatterEnd', jetType, QCDType)

preNum = {}
initNum = {}
extraNum = {}
forwardNum = {}
annulusNum = {}

preNumErr = {}
initNumErr = {}
extraNumErr = {}
forwardNumErr = {}
annulusNumErr = {}

for hist in annulus['ht']:
    preNumErr[hist] = rt.Double(0)
    initNumErr[hist] = rt.Double(0)
    extraNumErr[hist] = rt.Double(0)
    forwardNumErr[hist] = rt.Double(0)
    annulusNumErr[hist] = rt.Double(0)
for hist in pre['ht']:
    preNum[hist] = pre['ht'][hist].IntegralAndError(1,1000,preNumErr[hist])
for hist in init['ht']:
    initNum[hist] = init['ht'][hist].IntegralAndError(1,1000,initNumErr[hist])
for hist in extra['ht']:
    extraNum[hist] = extra['ht'][hist].IntegralAndError(1,1000,extraNumErr[hist])
for hist in forward['ht']:
    forwardNum[hist] = forward['ht'][hist].IntegralAndError(1,1000,forwardNumErr[hist])
for hist in annulus['ht']:
    annulusNum[hist] = annulus['ht'][hist].IntegralAndError(1,1000,annulusNumErr[hist])

preNum['Background'] = rt.Double(0)
initNum['Background'] = rt.Double(0)
extraNum['Background'] = rt.Double(0)
forwardNum['Background'] = rt.Double(0)
annulusNum['Background'] = rt.Double(0)
preNumErr['Background'] = rt.Double(0)
initNumErr['Background'] = rt.Double(0)
extraNumErr['Background'] = rt.Double(0)
forwardNumErr['Background'] = rt.Double(0)
annulusNumErr['Background'] = rt.Double(0)

preNum['Other'] = rt.Double(0)
initNum['Other'] = rt.Double(0)
extraNum['Other'] = rt.Double(0)
forwardNum['Other'] = rt.Double(0)
annulusNum['Other'] = rt.Double(0)
preNumErr['Other'] = rt.Double(0)
initNumErr['Other'] = rt.Double(0)
extraNumErr['Other'] = rt.Double(0)
forwardNumErr['Other'] = rt.Double(0)
annulusNumErr['Other'] = rt.Double(0)

preErrSum = rt.Double(0)
initErrSum = rt.Double(0)
extraErrSum = rt.Double(0)
forwardErrSum = rt.Double(0)
annulusErrSum = rt.Double(0)
preOtherErrSum = rt.Double(0)
initOtherErrSum = rt.Double(0)
extraOtherErrSum = rt.Double(0)
forwardOtherErrSum = rt.Double(0)
annulusOtherErrSum = rt.Double(0)

for hist in annulus['ht']:
    if 'Tbt' in hist or 'Ttt' in hist or 'TpTp' in hist or 'Data' in hist:
        continue
    if 'QCD' not in hist and 'TTJets' not in hist:
        preNum['Other'] += preNum[hist]
        initNum['Other'] += initNum[hist]
        extraNum['Other'] += extraNum[hist]
        forwardNum['Other'] += forwardNum[hist]
        annulusNum['Other'] += annulusNum[hist]
        preOtherErrSum += preNumErr[hist]*preNumErr[hist]
        initOtherErrSum += initNumErr[hist]*initNumErr[hist]
        extraOtherErrSum += extraNumErr[hist]*extraNumErr[hist]
        forwardOtherErrSum += forwardNumErr[hist]*forwardNumErr[hist]
        annulusOtherErrSum += annulusNumErr[hist]*annulusNumErr[hist]
       
    preNum['Background'] += preNum[hist]
    initNum['Background'] += initNum[hist]
    extraNum['Background'] += extraNum[hist]
    forwardNum['Background'] += forwardNum[hist]
    annulusNum['Background'] += annulusNum[hist]
    preErrSum += preNumErr[hist]*preNumErr[hist]
    initErrSum += initNumErr[hist]*initNumErr[hist]
    extraErrSum += extraNumErr[hist]*extraNumErr[hist]
    forwardErrSum += forwardNumErr[hist]*forwardNumErr[hist]
    annulusErrSum += annulusNumErr[hist]*annulusNumErr[hist]

preNumErr['Background'] = rt.TMath.Sqrt(preErrSum)
initNumErr['Background'] = rt.TMath.Sqrt(initErrSum)
extraNumErr['Background'] = rt.TMath.Sqrt(extraErrSum)
forwardNumErr['Background'] = rt.TMath.Sqrt(forwardErrSum)
annulusNumErr['Background'] = rt.TMath.Sqrt(annulusErrSum)
preNumErr['Other'] = rt.TMath.Sqrt(preOtherErrSum)
initNumErr['Other'] = rt.TMath.Sqrt(initOtherErrSum)
extraNumErr['Other'] = rt.TMath.Sqrt(extraOtherErrSum)
forwardNumErr['Other'] = rt.TMath.Sqrt(forwardOtherErrSum)
annulusNumErr['Other'] = rt.TMath.Sqrt(annulusOtherErrSum)

with open('eff_cuts/eventsCutflow_tZ_'+jetType+'_QCD'+QCDType+'_25Apr18.txt','w') as f:
    f.write('|      sample      |      presel      |      init      |      extra      |      forward      |      annulus      |\n')
    f.write('\nRaw:\n')
    for key in sorted(annulusNum):
        spacing = ' ' * (18-len(key))
        presel = str(TradRound(preNum[key]))+ ' \pm ' + str(TradRound(preNumErr[key]))
        init = str(TradRound(initNum[key])) + ' \pm ' +str(TradRound(initNumErr[key]))
        extra = str(TradRound(extraNum[key])) + ' \pm ' + str(TradRound(extraNumErr[key]))
        annulus = str(TradRound(annulusNum[key])) + ' \pm ' + str(TradRound(annulusNumErr[key]))
        forward = str(TradRound(forwardNum[key])) + ' \pm ' + str(TradRound(forwardNumErr[key]))

        if 'data' in key or 'Data' in key:
            continue
            f.write(' ' + str(key) + spacing +'& $'+ presel+'$' + ' ' * (20-len(presel)) +'& $'+ init+'$' + ' ' * (20-len(init)) +'& $'+ extra+'$' + ' ' * (20-len(extra)) + ' ' * (20-len(annulus)) +'& $'+ forward+'$' + ' ' * (20-len(forward)) + ' \\\\ \n')
        else:
            f.write(' ' + str(key) + spacing +'& $'+ presel+'$' + ' ' * (20-len(presel)) +'& $'+ init+'$' + ' ' * (20-len(init)) +'& $'+ extra+'$' + ' ' * (20-len(extra)) +'& $'+ forward+'$' + ' ' * (20-len(forward)) + '& $'+annulus+'$ \\\\' + '\n')
    f.close()

