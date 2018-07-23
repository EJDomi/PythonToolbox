#!/usr/bin/env python

import ROOT as rt
import array
from input_anaTp_cfi import *


if path.exists('weightFunctions.C'):
    rt.gROOT.Macro('weightFunctions.C')

def processTrees(dataSamples, bkgSamples, sigSamples):

    for samples in dataSamples:  


def readTree(inFile,jetType):
    '''
    Function to loop over the events of the given file and tree
    @inFile  : The file to be processed
    @jetType : The addendum to the directory the tree is in, 
               ex) ana<jetType>/tree is the location of the tree in any given file
               default: none
    '''
    f = rt.TFile(inFile, 'r')
    t = f.Get('ana'+jetType+'/tree')
 
    #Reserve variables and branch addresses here
    nAK8 = array.array('d', [0]) #Use of array allows for memory reference when setting branch address

    t.SetBranchAddress('SelectedEvent_nAK8', nAK8)

    #Loop over events in tree
    # Note: the ROOT method of running over events is faster than the python method i.e. 'for event in tree'
    for iEvent in xrange(t.GetEntries()):

        if iEvent % 100000 is 0:
            print iEvent

        t.GetEntry(iEvent) #fill reserved variables

        # Perform variable manipulation
        for jet in range(nAK8[0]):  #for looping over AK8 jets in event

        # Fill histograms
        # ex) h.Fill(nAK8[0])

if __name__ == "__main__":
    readTree('samples_v2/JetHT_2016B.root','CHS')
