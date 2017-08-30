cutsRegionA = {
               'Base' : 'isRegionA',
              }
cutsRegionB = {
               'Base' : 'isRegionB',
              }
cutsRegionC = {
               'Base' : 'isRegionC',
              }
cutsRegionD = { 
               'Base' : 'isRegionD',
             } 

additionalCuts = {
                  'top_3p0' : 'nAK8>=2&&ptAK8[0]>400&&PrunedMassAK8[0]>50&&(ptAK8[0]+ptAK8[1])>850',
                 } 

isRegionA_FOM = {
              'mtprimeDummyA' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*btagsf',
                       'SigWts' : 'EvtWeight*EvtWtPV*btagsf',
                       'Cuts'  :  cutsRegionA['Base'],
                       'xMin'  : '0',
                       'xMax'  : '3200',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
#              'nAK8[idxTopTagged]' : {
#                       'Wts'   : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,0)',
#                       'SigWts' : 'EvtWeight*EvtWtPV',
#                       'Cuts'  :  cutsRegionA['Base'],
#                       'xMin'  : '0',
#                       'xMax'  : '10',
#                       'nBins' : '11',
#                       'xLabel' : 'Num of AK8 jets [GeV]',
#                       'yLabel' : 'Jets',
#                       'log'   : True
#                     }
                }
isRegionB_FOM = {
              'mtprimeDummy' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*btagsf',
                       'SigWts' : 'EvtWeight*EvtWtPV*btagsf',
                       'Cuts'  :  cutsRegionB['Base'],
                       'xMin'  : '1100',
                       'xMax'  : '3200',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
#              'nAK8[idxTopTagged]' : {
#                       'Wts'   : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,0)',
#                       'SigWts' : 'EvtWeight*EvtWtPV',
#                       'Cuts'  :  cutsRegionB['Base'],
#                       'xMin'  : '0',
#                       'xMax'  : '10',
#                       'nBins' : '11',
#                       'xLabel' : 'Num of AK8 jets [GeV]',
#                       'yLabel' : 'Jets',
#                       'log'   : True
#                     }
                }
isRegionC_FOM = {
              'mtprimeDummyC' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*btagsf',
                       'SigWts' : 'EvtWeight*EvtWtPV*btagsf',
                       'Cuts'  : cutsRegionC['Base'],
                       'xMin'  : '1100',
                       'xMax'  : '3200',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
#              'nAK8[idxTopTagged]' : {
#                       'Wts'   : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,0)',
#                       'SigWts' : 'EvtWeight*EvtWtPV',
#                       'Cuts'  :  cutsRegionC['Base'],
#                       'xMin'  : '0',
#                       'xMax'  : '10',
#                       'nBins' : '11',
#                       'xLabel' : 'Num of AK8 jets [GeV]',
#                       'yLabel' : 'Jets',
#                       'log'   : True
#                     }
                }
isRegionD_FOM = {
              'mtprime' : {
                       #'Wts'   : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,0)',
                       'Wts'   : 'EvtWeight*EvtWtPV*btagsf',
                       'SigWts' : 'EvtWeight*EvtWtPV*btagsf',
                       'Cuts'  : cutsRegionD['Base'],
                       'xMin'  : '1100',
                       'xMax'  : '3200',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
#              'nAK8[idxTopTagged]' : {
#                       'Wts'   : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,0)',
#                       'SigWts' : 'EvtWeight*EvtWtPV',
#                       'Cuts'  :  cutsRegionD['Base'],
#                       'xMin'  : '0',
#                       'xMax'  : '10',
#                       'nBins' : '11',
#                       'xLabel' : 'Num of AK8 jets [GeV]',
#                       'yLabel' : 'Jets',
#                       'log'   : True
#                     }
                 }
