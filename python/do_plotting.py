#!/usr/bin/env python

from plotting import *
from variableDictionaries_cfi import *
from input_anaTp_cfi import *
def plot(dictionary, inFile, outDir = 'plots', doData = True, doFit = False, region = ''):
    for variable in dictionary:
        if '/' in variable:
            histDir = variable.split('/')[0]
        else:
            histDir = variable
        print 'Now Plotting: ' + histDir 
        xMin = float(dictionary[variable]['xMin'])
        xMax = float(dictionary[variable]['xMax'])
        nBins = float(dictionary[variable]['nBins'])
        xLabel = dictionary[variable]['xLabel']
        yLabel = dictionary[variable]['yLabel']
        #doLog = dictionary[variable]['log']
        doLog = True 
        DrawPlots(inFile, histDir, xMin, xMax, doFit, xLabel, yLabel, doLog, doData, histDir+'/', outDir, region)

if __name__ == '__main__':
    plot(preselDict_Wt, 'presel_QCDHT_Wt_noBtagSF_27Aug17.root', './presel_v3/QCDHT_Wt', True, False, '_QCDHT_Wt')
    plot(preselDict, 'presel_QCDPt_noBtagSF_27Aug17.root', './presel_v3/QCDPt', True, False, '_QCDPt')
#    plot(htDict, 'histFiles/ht_regionA_26Jun17.root', 'plots/ht_26Jun17', True, True, '_regionA')
#    plot(htDict, 'histFiles/ht_regionB_26Jun17.root', 'plots/ht_26Jun17', True, True, '_regionB')
#    plot(htDict, 'histFiles/ht_regionC_26Jun17.root', 'plots/ht_26Jun17', True, True, '_regionC')
#    plot(htDict, 'histFiles/ht_ttEnriched_1topTagged_noHtagged_noAntiH_26Jun17.root', 'plots/ht_26Jun17', True, True, '_1Top_noH_noAntiH')
#    plot(htDict, 'histFiles/ht_ttEnriched_2topTagged_26Jun17.root', 'plots/ht_26Jun17', True, True, '_2Top')
#    plot(htDict, 'histFiles/ht_ttEnriched_2topTagged_noHtagged_noAntiH_26Jun17.root', 'plots/ht_26Jun17', True, True, '_2Top_noH_noAntiH')
#    plot(htDict, 'histFiles/ht_ttEnriched_2topTagged_noHtagged_26Jun17.root', 'plots/ht_26Jun17', True, True, '_2Top_noH')
#    plot(preselDict, 'histFiles/presel_kin_sub_regionA_21Jun17.root', 'plots/26Jun17', True, False, '_presel_regionA')
#    plot(preselDict, 'histFiles/presel_kin_sub_regionB_21Jun17.root', 'plots/26Jun17', True, False, '_presel_regionB')
#    plot(preselDict, 'histFiles/presel_kin_sub_regionC_21Jun17.root', 'plots/26Jun17', True, False, '_presel_regionC')
    #plot(nJetsRegionA, 'histFiles/1Feb17/regionA_3p0.root', 'plots/1Feb17', True, False, '_regionA_3p0')
    #plot(nJetsRegionB, 'histFiles/1Feb17/regionB_3p0.root', 'plots/1Feb17', True, False, '_regionB_3p0')
    #plot(nJetsRegionC, 'histFiles/1Feb17/regionC_3p0.root', 'plots/1Feb17', True, False, '_regionC_3p0')
    #plot(nJetsRegionD, 'histFiles/1Feb17/regionD_3p0.root', 'plots/1Feb17', False, False, '_regionD_3p0')
    #plot(nJetsRegionA, 'histFiles/1Feb17/jetMultiplicity_regionA_2015.root', 'plots/1Feb17', True, False, '_regionA')
    #plot(nJetsRegionB, 'histFiles/1Feb17/jetMultiplicity_regionB_2015.root', 'plots/1Feb17', True, False, '_regionB')
    #plot(nJetsRegionC, 'histFiles/1Feb17/jetMultiplicity_regionC_2015.root', 'plots/1Feb17', True, False, '_regionC')
    #plot(nJetsRegionD, 'histFiles/1Feb17/jetMultiplicity_regionD_2015.root', 'plots/1Feb17', True, False, '_regionD')
    #plot(preselDict_HTWt, 'histFiles/1Feb17/presel_2015.root', 'plots/1Feb17', True, False)
    #plot(preselDict_HTWt, 'histFiles/17Jan17/test.root', 'plots/17Jan17', True, False)
