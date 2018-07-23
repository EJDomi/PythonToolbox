#!/usr/bin/env python

from plotting_new import *
from variableDictionaries_cfi import *
from input_anaTp_cfi import *
def plot(dictionary, inFile, outDir = 'plots', doData = True, doScale = False, region = ''):
    DrawPlots(inFile, dictionary, doData, doScale, outDir, region)

if __name__ == '__main__':
    #plot(mtprimeTildes, 'postfitshapes_TbtH_1200_30p.root', './plots/', True, False, '_TbtH_3Jul18')
    #plot(mtprimeTildes, 'postfitshapes_TbtZ_1200_30p.root', './plots/', True, False, '_TbtZ_3Jul18')
    plot(mtprimeTildes, 'postfitshapes_TttH_1200_30p.root', './plots/', True, False, '_TttH_5Jul18')
    #plot(mtprimeTildes, 'postfitshapes_TttZ_1200_30p.root', './plots/', True, False, '_TttZ_3Jul18')
    #plot(mtprimeTildes, 'postfitshapes_TbtZ_1200.root', './plots/', True, False, '_TbtZ_17Jun18')
    #plot(mtprimeTildes, 'postfitshapes_TbtHtZ_00p.root', './plots/', True, False, '_TbtHtZ_17Jun18')
    #plot(mtprimeTildes, 'postfitshapes_TttHtZ_00p.root', './plots/', True, False, '_TttHtZ_17Jun18')
    #plot(mtprimeTildes, 'plottingTemplate/templates_tZ_signal_26Apr18.root', './plots/', True, False, '_tZ_test_26')
    #plot(mtprimeTildes, 'plottingTemplate/templates_tH_signal_26Apr18.root', './plots/', False, False, '_tH_26')
    #plot(mtprimeTildes, 'plottingTemplate/templates_tZ_signal_26Apr18.root', './plots/', False, False, '_tZ_26')
    #plot(ptAK8, './histFiles/sjptAK8_topL_23Feb18.root', './plots/', True, False, '_topL')
    #plot(ptAK8, './histFiles/sjptAK8_topM_23Feb18.root', './plots/', True, False, '_topM_errorE')
    #plot(ptAK8, './histFiles/sjptAK8_massWindow_23Feb18.root', './plots/', True, False, '_massWindow')
    #plot(mtprimeTildes, './histFiles/mt_22Jun18.root', './plots/', True, False, '_22Jun18')
    #plot(preselDict, './histFiles/npv_4Apr18.root', './plots/5Apr18', True, False, '_presel')
    #plot(finalSel, './histFiles/ptZTagged_Z_21May18.root', './plots/', False, False, '_regionZ')
    #plot(mtprimeTildes, './histFiles/ptAK4_A_21May18.root', './plots/', True, False, '_regionA')
    #plot(mtprimeTildes, './histFiles/ptAK4_B_21May18.root', './plots/', True, False, '_regionB')
    #plot(mtprimeTildes, './histFiles/ptAK4_C_21May18.root', './plots/', True, False, '_regionC')
    #plot(mtprimeTildes, './histFiles/ptAK4_D_21May18.root', './plots/', False, False, '_regionD')
    #plot(mtprimeTildes, './histFiles/ptAK4_W_21May18.root', './plots/', True, False, '_regionW')
    #plot(mtprimeTildes, './histFiles/ptAK4_X_21May18.root', './plots/', True, False, '_regionX')
    #plot(mtprimeTildes, './histFiles/ptAK4_Y_21May18.root', './plots/', True, False, '_regionY')
    #plot(mtprimeTildes, './histFiles/ptAK4_Z_21May18.root', './plots/', False, False, '_regionZ')
    #plot(mtprimeTildes, './histFiles/mtprimeTildes_4Apr18.root', './plots/5Apr18', False, False, '_mtp')
    #plot(nTop, './histFiles/nTops_QCDPt_12Sep17.root', './plots', True, False, '_QCDPt')
    #plot(sumPtDict, './histFiles/sumPt_QCDPt_12Sep17.root', './plots', True, False, '_QCDPt')
    #plot(zTopMass, './histFiles/tPrimeMasses_signalRegion_QCDPt_12Sep17.root', './plots', False, True, '_QCDPt')
    #plot(forwardJets, './histFiles/forwardJets_signalRegion_QCDPt_12Sep17.root', './plots', False, True, '_QCDPt')
    #plot(preselDict_Wt, './histFiles/presel_QCDHT_12Sep17.root', './plots', True, False, '_QCDHT')
