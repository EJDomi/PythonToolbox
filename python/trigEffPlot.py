#!/usr/bin/env python

import ROOT as rt
import os, re, sys, optparse, commands, shutil, imp

helper = imp.load_source('fix', './help.py')
tdrstyle = imp.load_source('tdrstyle', './tdrstyle.py')
CMS_lumi = imp.load_source('CMS_lumi', './CMS_lumi.py')

def makePlot(inFile1, inFile2, histName, xLabel, yLabel, name):

  rt.gROOT.SetBatch()
  rt.gROOT.SetStyle('Plain')
  rt.gStyle.SetOptTitle(0) 
  rt.gStyle.SetOptStat(0000) 
  rt.gStyle.SetOptFit(0111) 
  rt.gStyle.SetErrorX(0.0001)

  fin1 = rt.TFile(inFile1, 'READ')
  fin2 = rt.TFile(inFile2, 'READ')
  rt.SetOwnership(fin1,True)
  rt.SetOwnership(fin2,True)

  hist1 = fin1.Get(histName)
  hist2 = fin2.Get(histName)
 
  c0 = rt.TCanvas('c_mc_'+histName.replace('/',''),'',600,600)
  tdrstyle.setTDRStyle() 
  tgr = rt.TGraphAsymmErrors()
  tgr.Divide(hist1, hist2)

  tgr.GetYaxis().SetTitle(yLabel)
  #tgr.GetYaxis().SetTitleOffset(tgr.GetYaxis().GetTitleOffset()+1.0)

  tgr.GetXaxis().SetTitle(xLabel)
  tgr.GetXaxis().SetLabelSize(0.03)
  
  tgr.Draw()
  leg = rt.TLegend(0.5,0.45,0.8,0.55)
  leg.SetBorderSize(0)
  leg.SetFillColor(0)
  leg.SetTextSize(0.022)
  if 'IsoMu' in name:
    leg.AddEntry(tgr, "Data preselection + HLT_IsoMu24","ep")
  elif 'Mu' in name:
    leg.AddEntry(tgr, "Data preselection + HLT_Mu50","ep")
  elif 'HT1050' in name:
    leg.AddEntry(tgr, "Data preselection + HLT_PFJet320","ep")
  #leg.Draw()
  # lumi text options
  #CMS_lumi.lumi_13TeV = "35.9/fb"
  #CMS_lumi.lumi_sqrtS = "tt+jets"
  if 'Mu' in name:
    CMS_lumi.lumi_sqrtS = "2018B"
  else:
    CMS_lumi.lumi_sqrtS = "2018B"
  CMS_lumi.writeExtraText = 1
  ##CMS_lumi.extraText = "Simulation"
  CMS_lumi.extraText = "Preliminary"

  iPos = 0
  if( iPos==0 ): CMS_lumi.relPosX = 0.18
  CMS_lumi.CMS_lumi(c0, 0, iPos, False, False)
  c0.SetGridx()
  c0.SetGridy()
  c0.SetLeftMargin(0.18)
  c0.SetRightMargin(0.08)
  c0.SetBottomMargin(0.15)
  c0.Update() 

  c0.SaveAs('./trigPlots/'+name+'.png')
  #input("waiting for editing...")
if __name__ == "__main__":
  #makePlot('./btagEff_TTJets_loose.root', 'tp_eff_b', 'subjet p_{T} [GeV]', 'b flavor efficiency')
  #makePlot('./btagEff_TTJets_loose.root', 'tp_eff_c', 'subjet p_{T} [GeV]', 'c flavor efficiency')
  #makePlot('./btagEff_TTJets_loose.root', 'tp_eff_l', 'subjet p_{T} [GeV]', 'l flavor efficiency')
  #makePlot('./btagEff_TTJets_medium.root', 'tp_eff_b', 'subjet p_{T} [GeV]', 'b flavor efficiency')
  #makePlot('./btagEff_TTJets_medium.root', 'tp_eff_c', 'subjet p_{T} [GeV]', 'c flavor efficiency')
  #makePlot('./btagEff_TTJets_medium.root', 'tp_eff_l', 'subjet p_{T} [GeV]', 'l flavor efficiency')
  #makePlot('./btagEffMaps/btagEff_Tbq_LH_loose.root', 'tp_eff_b', 'subjet p_{T} [GeV]', 'b flavor efficiency')
  #makePlot('./btagEffMaps/btagEff_Tbq_LH_loose.root', 'tp_eff_c', 'subjet p_{T} [GeV]', 'c flavor efficiency')
  #makePlot('./btagEffMaps/btagEff_Tbq_LH_loose.root', 'tp_eff_l', 'subjet p_{T} [GeV]', 'l flavor efficiency')
  #makePlot('./btagEffMaps/btagEff_Tbq_LH_medium.root', 'tp_eff_b', 'subjet p_{T} [GeV]', 'b flavor efficiency')
  #makePlot('./btagEffMaps/btagEff_Tbq_LH_medium.root', 'tp_eff_c', 'subjet p_{T} [GeV]', 'c flavor efficiency')
  #makePlot('./btagEffMaps/btagEff_Tbq_LH_medium.root', 'tp_eff_l', 'subjet p_{T} [GeV]', 'l flavor efficiency')
  #makePlot('./histFiles/numerator_trig.root', './histFiles/denominator_trig.root', 'ptAK8[0]+ptAK8[1]/Data', 'p_{T} Sum [GeV]', 'efficiency, HLT_PFHT1050', 'HT1050_PFJet320_eff_ptSum')
  #makePlot('./histFiles/numerator_Mu_trig.root', './histFiles/denominator_Mu_trig.root', 'ptAK8[0]+ptAK8[1]/Data', 'p_{T} Sum [GeV]', 'efficiency, HLT_PFHT1050', 'HT1050_Mu50_eff_ptSum')
  #makePlot('./histFiles/numerator_IsoMu_trig.root', './histFiles/denominator_IsoMu_trig.root', 'ptAK8[0]+ptAK8[1]/Data', 'p_{T} Sum [GeV]', 'efficiency, HLT_PFHT1050', 'HT1050_IsoMu24_eff_ptSum')
  #makePlot('./histFiles/numerator_trig.root', './histFiles/denominator_trig.root', 'ht/Data', 'H_{T} [GeV]', 'efficiency, HLT_PFHT1050', 'HT1050_PFJet320_eff_ht')
  #makePlot('./histFiles/numerator_Mu_trig.root', './histFiles/denominator_Mu_trig.root', 'ht/Data', 'H_{T} [GeV]', 'efficiency, HLT_PFHT1050', 'HT1050_Mu50_eff_ht')
  #makePlot('./histFiles/numerator_IsoMu_trig.root', './histFiles/denominator_IsoMu_trig.root', 'ht/Data', 'H_{T} [GeV]', 'efficiency, HLT_PFHT1050', 'HT1050_IsoMu24_eff_ht')

  makePlot('./histFiles/numerator_319077.root', './histFiles/denominator_319077.root', 'ht/Data', 'H_{T} [GeV]', 'efficiency, HLT_PFHT1050', 'HT1050_319077_eff_ht')
  makePlot('./histFiles/numerator_control.root', './histFiles/denominator_control.root', 'ht/Data', 'H_{T} [GeV]', 'efficiency, HLT_PFHT1050', 'HT1050_control_eff_ht')
  makePlot('./histFiles/numerator_HEMask.root', './histFiles/denominator_HEMask.root', 'ht/Data', 'H_{T} [GeV]', 'efficiency, HLT_PFHT1050', 'HT1050_HEMask_eff_ht')

  makePlot('./histFiles/numerator_319077.root', './histFiles/denominator_319077.root', 'ptAK8[0]+ptAK8[1]/Data', 'p_{T} Sum [GeV]', 'efficiency, HLT_PFHT1050', 'HT1050_319077_eff_ptSum')
  makePlot('./histFiles/numerator_control.root', './histFiles/denominator_control.root', 'ptAK8[0]+ptAK8[1]/Data', 'p_{T} Sum [GeV]', 'efficiency, HLT_PFHT1050', 'HT1050_control_eff_ptSum')
  makePlot('./histFiles/numerator_HEMask.root', './histFiles/denominator_HEMask.root', 'ptAK8[0]+ptAK8[1]/Data', 'p_{T} Sum [GeV]', 'efficiency, HLT_PFHT1050', 'HT1050_HEMask_eff_Sum')

  makePlot('./histFiles/numerator_319077.root', './histFiles/denominator_319077.root', 'etaAK8/Data', '#eta AK8 jets', 'efficiency, HLT_PFHT1050', 'HT1050_319077_eff_etaAK8')
  makePlot('./histFiles/numerator_control.root', './histFiles/denominator_control.root', 'etaAK8/Data', '#eta AK8 jets', 'efficiency, HLT_PFHT1050', 'HT1050_control_eff_etaAK8')
  makePlot('./histFiles/numerator_HEMask.root', './histFiles/denominator_HEMask.root', 'etaAK8/Data', '#eta AK8 jets', 'efficiency, HLT_PFHT1050', 'HT1050_HEMask_eff_etaAK8')

  makePlot('./histFiles/numerator_319077.root', './histFiles/denominator_319077.root', 'phiAK8/Data', '#phi AK8 jets', 'efficiency, HLT_PFHT1050', 'HT1050_319077_eff_phiAK8')
  makePlot('./histFiles/numerator_control.root', './histFiles/denominator_control.root', 'phiAK8/Data', '#phi AK8 jets', 'efficiency, HLT_PFHT1050', 'HT1050_control_eff_phiAK8')
  makePlot('./histFiles/numerator_HEMask.root', './histFiles/denominator_HEMask.root', 'phiAK8/Data', '#phi AK8 jets', 'efficiency, HLT_PFHT1050', 'HT1050_HEMask_eff_phiAK8')

  makePlot('./histFiles/numerator_319077.root', './histFiles/denominator_319077.root', 'abs(etaAK4)/Data', '#eta forward AK4 jets', 'efficiency, HLT_PFHT1050', 'HT1050_319077_eff_etaAK4')
  makePlot('./histFiles/numerator_control.root', './histFiles/denominator_control.root', 'abs(etaAK4)/Data', '#eta forward AK4 jets', 'efficiency, HLT_PFHT1050', 'HT1050_control_eff_etaAK4')
  makePlot('./histFiles/numerator_HEMask.root', './histFiles/denominator_HEMask.root', 'abs(etaAK4)/Data', '#eta forward AK4 jets', 'efficiency, HLT_PFHT1050', 'HT1050_HEMask_eff_etaAK4')

  makePlot('./histFiles/numerator_319077.root', './histFiles/denominator_319077.root', 'phiAK4/Data', '#phi forward AK4 jets', 'efficiency, HLT_PFHT1050', 'HT1050_319077_eff_phiAK4')
  makePlot('./histFiles/numerator_control.root', './histFiles/denominator_control.root', 'phiAK4/Data', '#phi forward AK4 jets', 'efficiency, HLT_PFHT1050', 'HT1050_control_eff_phiAK4')
  makePlot('./histFiles/numerator_HEMask.root', './histFiles/denominator_HEMask.root', 'phiAK4/Data', '#phi forward AK4 jets', 'efficiency, HLT_PFHT1050', 'HT1050_HEMask_eff_phiAK4')

