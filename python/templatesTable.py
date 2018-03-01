#!/usr/bin/env python

from optparse import OptionParser
import ROOT as rt
from math import *
from round20 import *

def TradRound(num):
    return round(num+10**(-len(str(num))-1),2)

parser = OptionParser()

parser.add_option('--doUnc',action='store_true',
                  dest='doUnc', default=True,
                  help='get Unc numbers'
                 )
parser.add_option('--doTex',action='store_true',
                  dest='doTex', default=True,
                  help='output table in laTex format'
                 )
parser.add_option('--doRead',action='store_true',
                  dest='doRead', default=False,
                  help='output table in readable format'
                 )

parser.add_option('-f', '--infile', action='store',
                  dest='inFileName', default='templates_tH_updatedShapes_6Feb18_smoothed.root',
                  help='template file name'
                 )
parser.add_option('-o', '--outfile', action='store',
                  dest='outFileName', default='table_tH_updatedShapes_6Feb18_smoothed.tex',
                  help='output table file name'
                 )

(options, args) = parser.parse_args()

if __name__ == "__main__":

    inFile = rt.TFile(options.inFileName,'r')

    rt.TH1.AddDirectory(rt.kFALSE)
    rt.TH1.SetDefaultSumw2()

# initialize dictionaries
    bkgrHists = {}
    bkgrHists['Nominal'] = {}
    if options.doUnc:
        bkgrHists['Up'] = {}
        bkgrHists['Down'] = {}

    bkgrNum = {}
    bkgrNum['Nominal'] = {}
    if options.doUnc:
        bkgrNum['Up'] = {}
        bkgrNum['Down'] = {}

    bkgrNumErr = {}
    bkgrNumErr['Stat'] = {}
    
    bkgrNumErr['Systematic'] = {}

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

# loop for getting numbers out of histograms
    for process in bkgrHists['Nominal']:
        bkgrNum['Nominal'][process] = {}
        bkgrNumErr['Stat'][process] = {}
        for region in bkgrHists['Nominal'][process]:
            bkgrNumErr['Stat'][process][region] = rt.Double(0)
            bkgrNum['Nominal'][process][region] = TradRound(bkgrHists['Nominal'][process][region].IntegralAndError(1,1000,bkgrNumErr['Stat'][process][region]))
            tmpErr = TradRound(bkgrNumErr['Stat'][process][region])
            bkgrNumErr['Stat'][process][region] = tmpErr 
    if options.doUnc:
        for process in bkgrHists['Up']:
            for region in bkgrHists['Up'][process]:
                for syst in bkgrHists['Up'][process][region]:
                    upErr = 0.
                    downErr = 0.
                    print process 
                    bkgrNum['Up'][process][region][syst] = TradRound(bkgrHists['Up'][process][region][syst].Integral(1,1000))
                    bkgrNum['Down'][process][region][syst] = TradRound(bkgrHists['Down'][process][region][syst].Integral(1,1000))

                    upErr = abs(bkgrNum['Up'][process][region][syst] - bkgrNum['Nominal'][process][region])
                    downErr = abs(bkgrNum['Down'][process][region][syst] - bkgrNum['Nominal'][process][region])

                    bkgrNumErr['Systematic'][process][region][syst] = TradRound(max(upErr, downErr))

# filling tables currently tex only
    if options.doTex:
        with open(options.outFileName,'w') as f:
            f.write('\\begin{table}[!hHtb]\n')
            f.write(' \\begin{center}\n')
            f.write('  \\caption{test}\n')
            f.write('  \\label{tab:systable}\n')
            f.write('  \\begin{tabular}{l|c|c|c|c}\n')
            f.write('   \\hline\n')
            f.write('   \\hline\n')
            f.write('   Sample & A & B & C & D \\\\\n')
            f.write('   \\hline\n')
            f.write('   \\hline\n')
            for process in sorted(bkgrNum['Nominal']):
                print bkgrNum['Nominal']
                print process
                if 'QCD' not in process and 'est' not in process or 'MC_QCD' in process:
                    f.write('   '+process.replace('_',' ')+' & $'+str(bkgrNum['Nominal'][process]['regionA'])+' $\\pm$ '+str(bkgrNumErr['Stat'][process]['regionA'])+'$ & $'+
                                                str(bkgrNum['Nominal'][process]['regionB'])+' \\pm '+str(bkgrNumErr['Stat'][process]['regionB'])+'$ & $'+
                                                str(bkgrNum['Nominal'][process]['regionC'])+' \\pm '+str(bkgrNumErr['Stat'][process]['regionC'])+'$ & $'+
                                                str(bkgrNum['Nominal'][process]['regionD'])+' \\pm '+str(bkgrNumErr['Stat'][process]['regionD'])+'$ \\\\\n')
                    if options.doUnc and 'Background' not in process:
                        f.write('   \\hline\n')
                        for syst  in bkgrNumErr['Systematic'][process]['regionA']:
                            f.write('   '+syst+' & $'+str(bkgrNumErr['Systematic'][process]['regionA'][syst])+'$ & $'+
                                                     str(bkgrNumErr['Systematic'][process]['regionB'][syst])+'$ & $'+
                                                     str(bkgrNumErr['Systematic'][process]['regionC'][syst])+'$ & $'+
                                                     str(bkgrNumErr['Systematic'][process]['regionD'][syst])+'$ \\\\\n')
                elif 'estQCD' in process:
                    f.write('   '+process+' & & & & $'+str(bkgrNum['Nominal'][process]['regionD'])+' \\pm '+str(bkgrNumErr['Stat'][process]['regionD'])+'$ \\\\\n')
                    if options.doUnc and 'Background' not in process:
                        f.write('   \\hline\n')
                        for syst  in bkgrNumErr['Systematic'][process]['regionD']:
                            f.write('   '+syst+' & & & & $'+str(bkgrNumErr['Systematic'][process]['regionD'][syst])+'$ \\\\\n')
                elif 'Background' not in process:
                    f.write('   '+process+' & $'+str(bkgrNum['Nominal'][process]['regionA'])+' \\pm '+str(bkgrNumErr['Stat'][process]['regionA'])+'$ & $'+
                                                str(bkgrNum['Nominal'][process]['regionB'])+' \\pm '+str(bkgrNumErr['Stat'][process]['regionB'])+'$ & $'+
                                                str(bkgrNum['Nominal'][process]['regionC'])+' \\pm '+str(bkgrNumErr['Stat'][process]['regionC'])+'$ \\\\\n')
                    if options.doUnc and 'Background' not in process:
                        f.write('   \\hline\n')
                        for syst  in bkgrNumErr['Systematic'][process]['regionA']:
                            f.write('   '+syst+' & $'+str(bkgrNumErr['Systematic'][process]['regionA'][syst])+'$ & $'+
                                                     str(bkgrNumErr['Systematic'][process]['regionB'][syst])+'$ & $'+
                                                     str(bkgrNumErr['Systematic'][process]['regionC'][syst])+'$ \\\\\n')
          
                f.write('   \\hline\n')
                f.write('   \\hline\n')
            f.write('   \\end{tabular}\n')
            f.write(' \\end{center}\n')
            f.write('\\end{table}\n')
            f.close()





            
            
                
