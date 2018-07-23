#!/usr/bin/env python

from optparse import OptionParser

import ROOT as rt

from input_anaTp_cfi import *

parser.add_option('-f', '--infile', action='store',
                  dest='inFileName', default='templates_tH_updatedShapes_6Feb18_smoothed.root',
                  help='template file name'
                 )
parser.add_option('-o', '--outfile', action='store',
                  dest='outFileName', default='table_tH_updatedShapes_6Feb18_smoothed.root',
                  help='output table file name'
                 )

(options, args) = parser.parse_args()

def getBkgHists():
    inFile = rt.TFile(options.inFileName,'r')

    rt.TH1.AddDirectory(rt.kFALSE)
    rt.TH1.SetDefaultSumw2()

# initialize dictionaries
    bkgrHists = {}
    bkgrHists['Nominal'] = {}
    if options.doUnc:
        bkgrHists['Up'] = {}
        bkgrHists['Down'] = {}


    inKeys = inFile.GetListOfKeys()

# loop for first level of histogram dicts
    for key in inKeys:
        keyString = str(key)
        histName = keyString.split('"')[1]
        process = histName.split('_')[2]
        region = histName.split('_')[1]
        if 'MC' in histName and 'est' not in histName:
            process = 'MC_'+histName.split('_')[3]
        elif 'MC' in histName and 'est' in histName:
            continue
        else:
            process = histName.split('_')[2]
 

        if 'TpTp' in histName or 'Tb' in histName or 'Tt' in histName: continue
        if 'data' in histName: continue
        bkgrHists['Nominal'][process] = {}
        if 'Background' not in process:
            bkgrHists['Up'][process] = {}
            bkgrHists['Down'][process] = {}
            bkgrNum['Up'][process] = {}
            bkgrNum['Down'][process] = {}
            bkgrNumErr['Stat'][process] = {}
            bkgrNumErr['Systematic'][process] = {}

# loop for second level of histogram dicts
    for key in inKeys:
        keyString = str(key)
        histName = keyString.split('"')[1]
        region = histName.split('_')[1]
        if 'MC' in histName and 'est' not in histName:
            process = 'MC_'+histName.split('_')[3]
        elif 'MC' in histName and 'est' in histName:
            continue
        else:
            process = histName.split('_')[2]

        if 'TpTp' in histName or 'Tb' in histName or 'Tt' in histName: continue
        if 'data' in histName: continue
        if 'Background' not in process:
            bkgrHists['Up'][process][region] = {}
            bkgrHists['Down'][process][region] = {}
            bkgrNum['Up'][process][region] = {}
            bkgrNum['Down'][process][region] = {}
            bkgrNumErr['Stat'][process][region] = {}
            bkgrNumErr['Systematic'][process][region] = {}

# loop for getting histograms
    for key in inKeys:
        keyString = str(key)
        histName = keyString.split('"')[1]
        region = histName.split('_')[1]
        if 'MC' in histName and 'est' not in histName:
            process = 'MC_'+histName.split('_')[3]
        elif 'MC' in histName and 'est' in histName:
            continue
        else:
            process = histName.split('_')[2]

        if 'TpTp' in histName or 'Tb' in histName or 'Tt' in histName: continue
        if 'data' in histName: continue

        if 'Up' not in histName and 'Down' not in histName:
            bkgrHists['Nominal'][process][region] = key.ReadObj().Clone(histName)

        if options.doUnc:
            if 'Background' not in histName:
                if 'Up' in histName:
                    if 'MC' in histName and 'est' not in histName:
                        bkgrHists['Up'][process][region][histName.split('_')[4].replace('Up','')] = key.ReadObj().Clone(histName)
                    else:
                        bkgrHists['Up'][process][region][histName.split('_')[3].replace('Up','')] = key.ReadObj().Clone(histName)
                if 'Down' in histName:
                    if 'MC' in histName and 'est' not in histName:
                        bkgrHists['Down'][process][region][histName.split('_')[4].replace('Down','')] = key.ReadObj().Clone(histName)
                    else:
                        bkgrHists['Down'][process][region][histName.split('_')[3].replace('Down','')] = key.ReadObj().Clone(histName)

    return bkgrHists

def getSigHists():
    inFile = rt.TFile(options.inFileName,'r')

    rt.TH1.AddDirectory(rt.kFALSE)
    rt.TH1.SetDefaultSumw2()

# initialize dictionaries
    sigHists = {}
    sigHists['Nominal'] = {}
    if options.doUnc:
        sigHists['Up'] = {}
        sigHists['Down'] = {}

    inKeys = inFile.GetListOfKeys()

# loop for first level of histogram dicts
    for key in inKeys:
        keyString = str(key)
        histName = keyString.split('"')[1]
        region = histName.split('_')[1]
 

        if not ('TpTp' in histName or 'Tb' in histName or 'Tt' in histName): continue
        if 'TpTp' in histName:
            process = histName.split('_')[2]+'_'+histName.split('_')[3]
        elif '0p' in histName or 'GeV' in histName:
            process = histName.split('_')[2]+'_'+histName.split('_')[3]+'_'+histName.split('_')[4]+'_'+histName.split('_')[5]
        else:
            process = histName.split('_')[2]+'_'+histName.split('_')[3]+'_'+histName.split('_')[4]


        sigHists['Nominal'][process] = {}
        sigHists['Up'][process] = {}
        sigHists['Down'][process] = {}

# loop for second level of histogram dicts
    for key in inKeys:
        keyString = str(key)
        histName = keyString.split('"')[1]
        region = histName.split('_')[1]

        if not ('TpTp' in histName or 'Tb' in histName or 'Tt' in histName): continue
        if 'TpTp' in histName:
            process = histName.split('_')[2]+'_'+histName.split('_')[3]
        elif '0p' in histName or 'GeV' in histName:
            process = histName.split('_')[2]+'_'+histName.split('_')[3]+'_'+histName.split('_')[4]+'_'+histName.split('_')[5]
        else:
            process = histName.split('_')[2]+'_'+histName.split('_')[3]+'_'+histName.split('_')[4]
        sigHists['Nominal'][process][region] = {}
        sigHists['Up'][process][region] = {}
        sigHists['Down'][process][region] = {}

# loop for getting histograms
    for key in inKeys:
        keyString = str(key)
        histName = keyString.split('"')[1]
        region = histName.split('_')[1]

        if not('TpTp' in histName or 'Tb' in histName or 'Tt' in histName): continue

        if 'TpTp' in histName:
            process = histName.split('_')[2]+'_'+histName.split('_')[3]
        elif '0p' in histName or 'GeV' in histName:
            process = histName.split('_')[2]+'_'+histName.split('_')[3]+'_'+histName.split('_')[4]+'_'+histName.split('_')[5]
        else:
            process = histName.split('_')[2]+'_'+histName.split('_')[3]+'_'+histName.split('_')[4]

        if 'Up' not in histName and 'Down' not in histName:
            sigHists['Nominal'][process][region] = key.ReadObj().Clone(histName)

        if options.doUnc:
            if 'Up' in histName:
                if 'TpTp' in histName:
                    sigHists['Up'][process][region][histName.split('_')[4].replace('Up','')] = key.ReadObj().Clone(histName)
                elif '0p' in histName or 'GeV' in histName:
                    sigHists['Up'][process][region][histName.split('_')[6].replace('Up','')] = key.ReadObj().Clone(histName)
                else:
                    sigHists['Up'][process][region][histName.split('_')[5].replace('Up','')] = key.ReadObj().Clone(histName)
            if 'Down' in histName:
                if 'TpTp' in histName:
                    sigHists['Down'][process][region][histName.split('_')[4].replace('Down','')] = key.ReadObj().Clone(histName)
                elif '0p' in histName or 'GeV' in histName:
                    sigHists['Down'][process][region][histName.split('_')[6].replace('Down','')] = key.ReadObj().Clone(histName)
                else:
                    sigHists['Down'][process][region][histName.split('_')[5].replace('Down','')] = key.ReadObj().Clone(histName)
  
    return sigHists


def plotSyst() 
    
    sigHists = getSigHists()
    bkgHists = getBkgHists()

    oFile = rt.TFile(options.outFileName, 'w')

    oFile.cd()
    regionADir = rt.gDirectory.mkdir('regionA')
    regionBDir = rt.gDirectory.mkdir('regionB')
    regionCDir = rt.gDirectory.mkdir('regionC')
    regionDDir = rt.gDirectory.mkdir('regionD')
    systDir = {}
    for region in bkgHists['TTJets']:
        if 'regionA' in region:
            regionADir.cd()
        elif 'regionB' in region:
            regionBDir.cd()
        elif 'regionC' in region:
            regionCDir.cd()
        elif 'regionD' in region:
            regionDDir.cd()
        systDir[region][syst] = {}
        for syst in bkgHists['TTJets'][region]:
            systDir[region][syst] = rt.gDirectory.mkdir(syst)

