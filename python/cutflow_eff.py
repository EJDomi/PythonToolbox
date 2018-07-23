#!/usr/bin/env python 

from anaTp import *
import re
from round20 import *
from variableDictionaries_cfi import *

jetType = 'CHS'
QCDType = 'Pt'
pre = analysis(Cutflow_pre, 'Nominal', 'Wts', 'SigWts', False, './dontMatterPre', jetType, QCDType)
init = analysis(Cutflow_init, 'Nominal', 'Wts', 'SigWts', False, './dontMatterHiggs', jetType, QCDType)
extra = analysis(Cutflow_extra, 'Nominal', 'Wts', 'SigWts', False, './dontMatterTop', jetType, QCDType)
forward = analysis(Cutflow_forward, 'Nominal', 'Wts', 'SigWts', False, './dontMatterEnd', jetType, QCDType)
annulus = analysis(Cutflow_annulus, 'Nominal', 'Wts', 'SigWts', False, './dontMatterEndZ', jetType, QCDType)

preNumEvts = {}
initNumEvts = {}
extraNumEvts = {}
forwardNumEvts = {}
annulusNumEvts = {}
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

for hist in pre['ht']:
    if 'Mtt' in hist or 'ST_t' in hist or 'QCD' in hist or 'Data' in hist:
        continue
    preNum[hist] = pre['ht'][hist].Integral(1,1000)/(lumi*sampleXsec[hist])
    preNumEvts[hist] = preNum[hist] * nEvts[hist]
    preNumErr[hist] = (1/nEvts[hist])*rt.TMath.Sqrt(preNumEvts[hist]*(1-(preNumEvts[hist]/nEvts[hist]))) 
for hist in init['ht']:
    if 'Mtt' in hist or 'ST_t' in hist or 'QCD' in hist or 'Data' in hist:
        continue
    initNum[hist] = init['ht'][hist].Integral(1,1000)/(lumi*sampleXsec[hist])
    initNumEvts[hist] = initNum[hist] * nEvts[hist]
    #initNum[hist] = initNumEvts[hist] / preNumEvts[hist]
    initNumErr[hist] = (1/preNumEvts[hist])*rt.TMath.Sqrt(initNumEvts[hist]*(1-(initNumEvts[hist]/preNumEvts[hist]))) 
for hist in extra['ht']:
    if 'Mtt' in hist or 'ST_t' in hist or 'QCD' in hist or 'Data' in hist:
        continue
    extraNum[hist] = extra['ht'][hist].Integral(1,1000)/(lumi*sampleXsec[hist])
    extraNumEvts[hist] = extraNum[hist] * nEvts[hist]
    #extraNum[hist] = extraNumEvts[hist] / preNumEvts[hist]
    extraNumErr[hist] = (1/preNumEvts[hist])*rt.TMath.Sqrt(extraNumEvts[hist]*(1-(extraNumEvts[hist]/preNumEvts[hist]))) 
for hist in forward['ht']:
    if 'Mtt' in hist or 'ST_t' in hist or 'QCD' in hist or 'Data' in hist:
        continue
    forwardNum[hist] = forward['ht'][hist].Integral(1,1000)/(lumi*sampleXsec[hist])
    forwardNumEvts[hist] = forwardNum[hist] * nEvts[hist]
    #forwardNum[hist] = forwardNumEvts[hist] / preNumEvts[hist]
    forwardNumErr[hist] = (1/preNumEvts[hist])*rt.TMath.Sqrt(forwardNumEvts[hist]*(1-(forwardNumEvts[hist]/preNumEvts[hist]))) 
for hist in annulus['ht']:
    if 'Mtt' in hist or 'ST_t' in hist or 'QCD' in hist or 'Data' in hist:
        continue
    annulusNum[hist] = annulus['ht'][hist].Integral(1,1000)/(lumi*sampleXsec[hist])
    annulusNumEvts[hist] = annulusNum[hist] * nEvts[hist]
    #annulusNum[hist] = annulusNumEvts[hist] / preNumEvts[hist]
    annulusNumErr[hist] = (1/preNumEvts[hist])*rt.TMath.Sqrt(annulusNumEvts[hist]*(1-(annulusNumEvts[hist]/preNumEvts[hist]))) 



with open('eff_cuts/efficiencies_tZ_'+jetType+'_QCD'+QCDType+'_26Apr18.txt','w') as f:
    f.write('|   hist   |   presel   |   init   |    extra    |   forward   |   annulus   |\n')
    
    f.write('\n Raw:\n')
    for key in sorted(preNum):
        spacing = ' ' * (18-len(key))
        presel = str(preNum[key])+ ' \pm ' + str(preNumErr[key])
        initial = str(initNum[key]) + ' \pm ' +str(initNumErr[key])
        extraJets = str(extraNum[key]) + ' \pm ' + str(extraNumErr[key])
        forwardJets = str(forwardNum[key]) + ' \pm ' + str(forwardNumErr[key])
        annulusCut = str(annulusNum[key]) + ' \pm ' + str(annulusNumErr[key])

        f.write(' ' + str(key) + spacing + presel + ' ' *(50-len(presel)) + initial + ' ' * (50-len(initial)) + extraJets + ' ' * (50-len(extraJets)) + forwardJets + ' ' * (50-len(forwardJets)) + annulusCut + '\n')

    f.write('\n Rounded:\n')
    for key in sorted(preNum):
        spacing = ' ' * (18-len(key))
        print key
        print preNum[key], preNumErr[key]
        preNumRound, preNumErrRound = roundOffErr(preNum[key], preNumErr[key])
        initialNumRound, initialNumErrRound = roundOffErr(initNum[key], initNumErr[key])
        extraJetsNumRound, extraJetsNumErrRound = roundOffErr(extraNum[key], extraNumErr[key])
        forwardJetsNumRound, forwardJetsNumErrRound = roundOffErr(forwardNum[key], forwardNumErr[key])
        annulusCutNumRound, annulusCutNumErrRound = roundOffErr(annulusNum[key], annulusNumErr[key])

        presel = str(preNumRound)+ ' \pm ' + str(preNumErrRound)
        initial = str(initialNumRound) + ' \pm ' +str(initialNumErrRound)
        extraJets = str(extraJetsNumRound) + ' \pm ' + str(extraJetsNumErrRound)
        forwardJets = str(forwardJetsNumRound) + ' \pm ' + str(forwardJetsNumErrRound)
        annulusCut = str(annulusCutNumRound) + ' \pm ' + str(annulusCutNumErrRound)

        f.write(' ' + str(key) + spacing + presel + ' ' * (30-len(presel)) + initial + ' ' * (30-len(initial)) + extraJets + ' ' * (30-len(extraJets)) + forwardJets + ' ' * (30-len(forwardJets)) + annulusCut + '\n')
    f.close()
