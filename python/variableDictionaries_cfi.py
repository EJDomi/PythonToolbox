#!/usr/bin/env python
import ROOT as rt
sumPtDict = {
                'ptAK8[0]+ptAK8[1]' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850 && PrunedMassAK8[0]>50&&ptAK8[0]>400',
                    'xMin'   : '0',
                    'xMax'   : '4000',
                    'nBins'  : '200',
                    'xLabel' : 'Scalar Sum p_{T} of Leading 2 AK8 jets [GeV]',
                    'yLabel' : 'Events/20GeV',
                    'log'    : True
                  },
}
preselDict = {
#                'npv' 
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.',
#                    'xMax'   : '50.',
#                    'nBins'  : '50',
#                    'xLabel' : 'nPV',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                'ptAK8[0]+ptAK8[1]' 
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : 'PrunedMassAK8[0]>50&&ptAK8[0]>400',
#                    'xMin'   : '0',
#                    'xMax'   : '4000',
#                    'nBins'  : '200',
#                    'xLabel' : 'Scalar Sum p_{T} of Leading 2 AK8 jets [GeV]',
#                    'yLabel' : 'Events/20GeV',
#                    'log'    : True
#                  },
#                'ht' 
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0',
#                    'xMax'   : '3000.',
#                    'nBins'  : '40',
#                    'xLabel' : 'H_{T} [GeV]',
#                    'yLabel' : 'Events/75GeV',
#                    'log'    : True
#                  },
#                'ptAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '200', 
#                    'xMax'   : '3000.', 
#                    'nBins'  : '140',
#                    'xLabel' : 'p_{T} 2 leading AK8 Jets [GeV]',
#                    'yLabel' : 'Jets/20GeV',
#                    'log'    : True
#                  },
#                'etaAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '-5.', 
#                    'xMax'   : '5.', 
#                    'nBins'  : '50',
#                    'xLabel' : '#eta 2 leading AK8 Jets',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'PrunedMassAK8' 
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.',
#                    'xMax'   : '800.',
#                    'nBins'  : '40',
#                    'xLabel' : 'Pruned Mass, 2 leading AK8 jets [GeV]',
#                    'yLabel' : 'Jets/20 geV',
#                    'log'    : True
#                  },
#                'SoftDropMassAK8' 
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.',
#                    'xMax'   : '800.',
#                    'nBins'  : '40',
#                    'xLabel' : 'Soft Drop Mass, leading AK8 jet [GeV]',
#                    'yLabel' : 'Jets/20 GeV',
#                    'log'    : True
#                  },
#                'tau2AK8/tau1AK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '50',
#                    'xLabel' : '#tau_{21}, 2 leading AK8 jets',
#                    'yLabel' : 'Jets',
#                    'log'    : True 
#                  },
#                'tau3AK8/tau2AK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '50',
#                    'xLabel' : '#tau_{32}, 2 leading AK8 jets',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'min(sj0CSVAK8,sj1CSVAK8)'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '20',
#                    'xLabel' : '2nd Highest CSVv2 discriminator, 2 leading AK8 jet',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'sj0CSVAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '20',
#                    'xLabel' : 'subjet 0 CSVv2 discriminator, 2 leading AK8 jets',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'sj1CSVAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '20',
#                    'xLabel' : 'subjet 1 CSVv2 discriminator, 2 leading AK8 jets',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'doubleBAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '-1', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '40',
#                    'xLabel' : 'Double B tagger discriminator, 2 leading AK8 jet',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'ptAK4'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.', 
#                    'xMax'   : '2000.', 
#                    'nBins'  : '100',
#                    'xLabel' : 'p_{T} AK4 Jets [GeV]',
#                    'yLabel' : 'Jets/20 GeV',
#                    'log'    : True
#                  },
#                'etaAK4'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '-5.', 
#                    'xMax'   : '5.', 
#                    'nBins'  : '50',
#                    'xLabel' : '#eta AK4 Jets [GeV]',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'nAK4'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0', 
#                    'xMax'   : '25', 
#                    'nBins'  : '25',
#                    'xLabel' : 'nAK4 Jets [GeV]',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'nAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0', 
#                    'xMax'   : '10', 
#                    'nBins'  : '10',
#                    'xLabel' : 'nAK8 Jets [GeV]',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                '@idxHTagged.size()'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*btagsf',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*btagsf',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0', 
#                    'xMax'   : '8', 
#                    'nBins'  : '8',
#                    'xLabel' : 'n Higgs tagged Jets [GeV]',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                '@idxTopTagged.size()'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*btagsf',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*btagsf',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0', 
#                    'xMax'   : '8', 
#                    'nBins'  : '8',
#                    'xLabel' : 'n top tagged Jets [GeV]',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
                '@idxZTagged.size()'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*btagsf',
                    'SigWts'    : 'EvtWeight*EvtWtPV*btagsf',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0', 
                    'xMax'   : '8', 
                    'nBins'  : '8',
                    'xLabel' : 'n Z tagged Jets [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
#		'costheta(ptAK8[idxAK8[0]],etaAK8[idxAK8[0]],phiAK8[idxAK8[0]],MAK8[idxAK8[0]],ptAK8[idxAK8[1]],etaAK8[idxAK8[1]],phiAK8[idxAK8[1]],MAK8[idxAK8[1]])'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '-1',
#                    'xMax'   : '1',
#                    'nBins'  : '20',
#                    'xLabel' : 'Cos(#theta^{*})_{leading AK8 jets}',
#                    'yLabel' : 'Events/0.1',
#                    'log'    : True
#                  },
#                'gammabeta(ptAK8[idxAK8[0]],etaAK8[idxAK8[0]],phiAK8[idxAK8[0]],MAK8[idxAK8[0]],ptAK8[idxAK8[1]],etaAK8[idxAK8[1]],phiAK8[idxAK8[1]],MAK8[idxAK8[1]])'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0',
#                    'xMax'   : '5',
#                    'nBins'  : '50',
#                    'xLabel' : '#gamma#beta_{2 leading AK8 jets}',
#                    'yLabel' : 'Events/0.2',
#                    'log'    : True
#		},
#		'cos(delPhi(ptAK8[idxAK8[0]],etaAK8[idxAK8[0]],phiAK8[idxAK8[0]],MAK8[idxAK8[0]],ptAK8[idxAK8[1]],etaAK8[idxAK8[1]],phiAK8[idxAK8[1]],MAK8[idxAK8[1]]))'
#                : { 
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '-1',
#                    'xMax'   : '1',
#                    'nBins'  : '25',
#                    'xLabel' : 'Cos(#Delta#phi_{leading AK8 jets}',
#                    'yLabel' : 'Events',
#                    'log'    : True
#                  } ,
#		'delEta(etaAK8[idxAK8[0]],etaAK8[idxAK8[1]])'
#                : { 
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '-5',
#                    'xMax'   : '5',
#                    'nBins'  : '50',
#                    'xLabel' : '#Delta#eta_{leading AK8 jets}',
#                    'yLabel' : 'Events/0.2',
#                    'log'    : True
#                  } ,
#                'dR(etaAK8[0],phiAK8[0],etaAK8[1],phiAK8[1])'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0',
#                    'xMax'   : '7',
#                    'nBins'  : '35',
#                    'xLabel' : '#DeltaR_{leading AK8 jets}',
#                    'yLabel' : 'Events',
#                    'log'    : True
#                  } ,
#                'Mjj(ptAK8[idxAK8[0]],etaAK8[idxAK8[0]],phiAK8[idxAK8[0]],MAK8[idxAK8[0]],ptAK8[idxAK8[1]],etaAK8[idxAK8[1]],phiAK8[idxAK8[1]],MAK8[idxAK8[1]])'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '850',
#                    'xMax'   : '4000',
#                    'nBins'  : '63',
#                    'xLabel' : 'M_{jj} [GeV]',
#                    'yLabel' : 'Events/50 GeV',
#                    'log'    : True
#                  } ,
  
             }
preselDict_Wt = {
#                'npv' 
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.',
#                    'xMax'   : '50.',
#                    'nBins'  : '50',
#                    'xLabel' : 'nPV',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
                'ptAK8[0]+ptAK8[1]' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : 'PrunedMassAK8[0]>50&&ptAK8[0]>400',
                    'xMin'   : '0',
                    'xMax'   : '4000',
                    'nBins'  : '200',
                    'xLabel' : 'Scalar Sum p_{T} of Leading 2 AK8 jets [GeV]',
                    'yLabel' : 'Events/20GeV',
                    'log'    : True
                  },
#                'ht' 
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0',
#                    'xMax'   : '3000.',
#                    'nBins'  : '40',
#                    'xLabel' : 'H_{T} [GeV]',
#                    'yLabel' : 'Events/75GeV',
#                    'log'    : True
#                  },
#                'ptAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '200', 
#                    'xMax'   : '3000.', 
#                    'nBins'  : '140',
#                    'xLabel' : 'p_{T} 2 leading AK8 Jets [GeV]',
#                    'yLabel' : 'Jets/20GeV',
#                    'log'    : True
#                  },
#                'etaAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '-5.', 
#                    'xMax'   : '5.', 
#                    'nBins'  : '50',
#                    'xLabel' : '#eta 2 leading AK8 Jets',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'PrunedMassAK8' 
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.',
#                    'xMax'   : '800.',
#                    'nBins'  : '40',
#                    'xLabel' : 'Pruned Mass, 2 leading AK8 jets [GeV]',
#                    'yLabel' : 'Jets/20 geV',
#                    'log'    : True
#                  },
#                'SoftDropMassAK8' 
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.',
#                    'xMax'   : '800.',
#                    'nBins'  : '40',
#                    'xLabel' : 'Soft Drop Mass, leading AK8 jet [GeV]',
#                    'yLabel' : 'Jets/20 GeV',
#                    'log'    : True
#                  },
#                'tau2AK8/tau1AK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '50',
#                    'xLabel' : '#tau_{21}, 2 leading AK8 jets',
#                    'yLabel' : 'Jets',
#                    'log'    : True 
#                  },
#                'tau3AK8/tau2AK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '50',
#                    'xLabel' : '#tau_{32}, 2 leading AK8 jets',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'min(sj0CSVAK8,sj1CSVAK8)'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '20',
#                    'xLabel' : '2nd Highest CSVv2 discriminator, 2 leading AK8 jet',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'sj0CSVAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '20',
#                    'xLabel' : 'subjet 0 CSVv2 discriminator, 2 leading AK8 jets',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'sj1CSVAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '20',
#                    'xLabel' : 'subjet 1 CSVv2 discriminator, 2 leading AK8 jets',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'doubleBAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&&(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '-1', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '40',
#                    'xLabel' : 'Double B tagger discriminator, 2 leading AK8 jet',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'ptAK4'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0.', 
#                    'xMax'   : '2000.', 
#                    'nBins'  : '100',
#                    'xLabel' : 'p_{T} AK4 Jets [GeV]',
#                    'yLabel' : 'Jets/20 GeV',
#                    'log'    : True
#                  },
#                'etaAK4'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '-5.', 
#                    'xMax'   : '5.', 
#                    'nBins'  : '50',
#                    'xLabel' : '#eta AK4 Jets [GeV]',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'nAK4'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0', 
#                    'xMax'   : '25', 
#                    'nBins'  : '25',
#                    'xLabel' : 'nAK4 Jets [GeV]',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                'nAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0', 
#                    'xMax'   : '10', 
#                    'nBins'  : '10',
#                    'xLabel' : 'nAK8 Jets [GeV]',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                '@idxHTagged.size()'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*btagsf*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*btagsf*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0', 
#                    'xMax'   : '8', 
#                    'nBins'  : '8',
#                    'xLabel' : 'n Higgs tagged Jets [GeV]',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
#                '@idxTopTagged.size()'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*btagsf*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*btagsf*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0', 
#                    'xMax'   : '8', 
#                    'nBins'  : '8',
#                    'xLabel' : 'n top tagged Jets [GeV]',
#                    'yLabel' : 'Jets',
#                    'log'    : True
#                  },
                '@ptZTagged.size()'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*btagsf*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*btagsf*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0', 
                    'xMax'   : '8', 
                    'nBins'  : '8',
                    'xLabel' : 'n Z tagged Jets [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
#		'costheta(ptAK8[idxAK8[0]],etaAK8[idxAK8[0]],phiAK8[idxAK8[0]],MAK8[idxAK8[0]],ptAK8[idxAK8[1]],etaAK8[idxAK8[1]],phiAK8[idxAK8[1]],MAK8[idxAK8[1]])'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '-1',
#                    'xMax'   : '1',
#                    'nBins'  : '20',
#                    'xLabel' : 'Cos(#theta^{*})_{leading AK8 jets}',
#                    'yLabel' : 'Events/0.1',
#                    'log'    : True
#                  },
#                'gammabeta(ptAK8[idxAK8[0]],etaAK8[idxAK8[0]],phiAK8[idxAK8[0]],MAK8[idxAK8[0]],ptAK8[idxAK8[1]],etaAK8[idxAK8[1]],phiAK8[idxAK8[1]],MAK8[idxAK8[1]])'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0',
#                    'xMax'   : '5',
#                    'nBins'  : '50',
#                    'xLabel' : '#gamma#beta_{2 leading AK8 jets}',
#                    'yLabel' : 'Events/0.2',
#                    'log'    : True
#		},
#		'cos(delPhi(ptAK8[idxAK8[0]],etaAK8[idxAK8[0]],phiAK8[idxAK8[0]],MAK8[idxAK8[0]],ptAK8[idxAK8[1]],etaAK8[idxAK8[1]],phiAK8[idxAK8[1]],MAK8[idxAK8[1]]))'
#                : { 
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '-1',
#                    'xMax'   : '1',
#                    'nBins'  : '25',
#                    'xLabel' : 'cos(#Delta#phi_{leading AK8 jets})',
#                    'yLabel' : 'Events',
#                    'log'    : True
#                  } ,
#		'delEta(etaAK8[idxAK8[0]],etaAK8[idxAK8[1]])'
#                : { 
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '-5',
#                    'xMax'   : '5',
#                    'nBins'  : '50',
#                    'xLabel' : '#Delta#eta_{leading AK8 jets}',
#                    'yLabel' : 'Events/0.2',
#                    'log'    : True
#                  } ,
#                'dR(etaAK8[0],phiAK8[0],etaAK8[1],phiAK8[1])'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '0',
#                    'xMax'   : '7',
#                    'nBins'  : '35',
#                    'xLabel' : '#Delta R_{leading AK8 jets}',
#                    'yLabel' : 'Events',
#                    'log'    : True
#                  } ,
#                'Mjj(ptAK8[idxAK8[0]],etaAK8[idxAK8[0]],phiAK8[idxAK8[0]],MAK8[idxAK8[0]],ptAK8[idxAK8[1]],etaAK8[idxAK8[1]],phiAK8[idxAK8[1]],MAK8[idxAK8[1]])'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
#                    'xMin'   : '850',
#                    'xMax'   : '4000',
#                    'nBins'  : '63',
#                    'xLabel' : 'M_{jj} [GeV]',
#                    'yLabel' : 'Events/50 GeV',
#                    'log'    : True
#                  } ,
  
             }
leadingJets = {
                'PrunedMassAK8[0]' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0.',
                    'xMax'   : '800.',
                    'nBins'  : '40',
                    'xLabel' : 'Pruned Mass, leading AK8 jet [GeV]',
                    'yLabel' : 'Jets/20 geV',
                    'log'    : True
                  },
                'SoftDropMassAK8[0]' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0.',
                    'xMax'   : '800.',
                    'nBins'  : '40',
                    'xLabel' : 'Soft Drop Mass, leading AK8 jet [GeV]',
                    'yLabel' : 'Jets/20 GeV',
                    'log'    : True
                  },
                'tau2AK8[0]/tau1AK8[0]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0.', 
                    'xMax'   : '1.', 
                    'nBins'  : '50',
                    'xLabel' : '#tau_{21}, leading AK8 jet',
                    'yLabel' : 'Jets',
                    'log'    : True 
                  },
             
                'tau3AK8[0]/tau2AK8[0]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0.', 
                    'xMax'   : '1.', 
                    'nBins'  : '50',
                    'xLabel' : '#tau_{32}, leading AK8 jet',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
                'ptAK8[0]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '200', 
                    'xMax'   : '3000.', 
                    'nBins'  : '140',
                    'xLabel' : 'p_{T} leading AK8 Jet [GeV]',
                    'yLabel' : 'Jets/20GeV',
                    'log'    : True
                  },
                'etaAK8[0]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '-5.', 
                    'xMax'   : '5.', 
                    'nBins'  : '50',
                    'xLabel' : '#eta leading AK8 Jet [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
                'min(sj0CSVAK8[0],sj1CSVAK8[0])'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0.', 
                    'xMax'   : '1.', 
                    'nBins'  : '20',
                    'xLabel' : '2nd Highest CSVv2 discriminator, leading AK8 jet',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
                'sj0CSVAK8[0]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0.', 
                    'xMax'   : '1.', 
                    'nBins'  : '20',
                    'xLabel' : 'leading AK8 subjet 0 CSVv2 discriminator',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
                'sj1CSVAK8[0]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0.', 
                    'xMax'   : '1.', 
                    'nBins'  : '20',
                    'xLabel' : 'leading AK8 subjet 1 AK8 CSVv2 discriminator',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
                'doubleBAK8[0]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '-1', 
                    'xMax'   : '1.', 
                    'nBins'  : '40',
                    'xLabel' : 'Double B tagger discriminator, leading AK8 jet',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
                'PrunedMassAK8[1]' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0.',
                    'xMax'   : '800.',
                    'nBins'  : '40',
                    'xLabel' : 'Pruned Mass, 2nd leading AK8 jet [GeV]',
                    'yLabel' : 'Jets/20 geV',
                    'log'    : True
                  },
                'SoftDropMassAK8[1]' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0.',
                    'xMax'   : '800.',
                    'nBins'  : '40',
                    'xLabel' : 'Soft Drop Mass, 2nd leading AK8 jet [GeV]',
                    'yLabel' : 'Jets/20 GeV',
                    'log'    : True
                  },
                'tau2AK8[1]/tau1AK8[1]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts' : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0.', 
                    'xMax'   : '1.', 
                    'nBins'  : '50',
                    'xLabel' : '#tau_{21}, 2nd leading AK8 jet',
                    'yLabel' : 'Jets',
                    'log'    : True 
                  },
             
                'tau3AK8[1]/tau2AK8[1]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0.', 
                    'xMax'   : '1.', 
                    'nBins'  : '50',
                    'xLabel' : '#tau_{32}, 2nd leading AK8 jet',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
                'ptAK8[1]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '200', 
                    'xMax'   : '3000.', 
                    'nBins'  : '140',
                    'xLabel' : 'p_{T} 2nd leading AK8 Jet [GeV]',
                    'yLabel' : 'Jets/20GeV',
                    'log'    : True
                  },
                'etaAK8[1]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '-5.', 
                    'xMax'   : '5.', 
                    'nBins'  : '50',
                    'xLabel' : '#eta 2nd leading AK8 Jet [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
                'min(sj0CSVAK8[0],sj1CSVAK8[0])'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0.', 
                    'xMax'   : '1.', 
                    'nBins'  : '20',
                    'xLabel' : '2nd Highest CSVv2 discriminator, 2nd leading AK8 jet',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
                'sj0CSVAK8[1]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0.', 
                    'xMax'   : '1.', 
                    'nBins'  : '20',
                    'xLabel' : '2nd leading AK8 subjet 0 CSVv2 discriminator',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
                'sj1CSVAK8[1]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '0.', 
                    'xMax'   : '1.', 
                    'nBins'  : '20',
                    'xLabel' : '2nd leading AK8 subjet 1 CSVv2 discriminator',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
                'doubleBAK8[1]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'SigWts'    : 'EvtWeight*EvtWtPV*WeightSumPt(ptAK8[0],ptAK8[1],0)',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&PrunedMassAK8[idxAK8[0]]>50&&ptAK8[idxAK8[0]]>400',
                    'xMin'   : '-1', 
                    'xMax'   : '1.', 
                    'nBins'  : '40',
                    'xLabel' : 'Double B tagger discriminator, 2nd leading AK8 jet',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
}
forwardJetsTuning = {
              'ht'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&Sum$(abs(etaAK4)>2.4)>0',
                    'xMin'   : '1100',
                    'xMax'   : '3100',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/80GeV',
                    'log'    : True
                  },     
                'etaAK4'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&isRegionD&&Max$(abs(etaAK4))',
                    'xMin'   : '0',
                    'xMax'   : '5',
                    'nBins'  : '50',
                    'xLabel' : '#eta AK4 Jets [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
} 
forwardJetsTuning_allSel = {
                'ht'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&isRegionD',
                    'xMin'   : '0',
                    'xMax'   : '5',
                    'nBins'  : '50',
                    'xLabel' : '#eta forward most AK4 Jet [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
} 
forwardJetsTuning_allSel_more1p5 = {
                'ht'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&isRegionD&&Max$(abs(etaAK4))>1.5',
                    'xMin'   : '0',
                    'xMax'   : '5',
                    'nBins'  : '50',
                    'xLabel' : '#eta AK4 Jets [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
} 
forwardJetsTuning_allSel_more2p4 = {
                'ht'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&isRegionD&&Max$(abs(etaAK4))>2.4',
                    'xMin'   : '0',
                    'xMax'   : '5',
                    'nBins'  : '50',
                    'xLabel' : '#eta AK4 Jets [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
} 

Cutflow_pre = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&ptAK8[0]>400 && prunedMassAK8[0]>50 && nAK8>=2 ',
                    'xMin'   : '0',
                    'xMax'   : '4000',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/80GeV',
                    'log'    : True
                  },
             }

Cutflow_higgs = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*btagsf',
                    'SigWts' : 'EvtWeight*EvtWtPV*btagsf',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&ptAK8[0]>400 && prunedMassAK8[0]>50 && nAK8>=2 && @ptHTagged.size()>0',
                    'xMin'   : '0',
                    'xMax'   : '4000',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/42GeV',
                    'log'    : True
                  },
               }
Cutflow_top = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*topSF(ptTopTagged)*btagsf',
                    'SigWts' : 'EvtWeight*EvtWtPV*topSF(ptTopTagged)*btagsf',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&ptAK8[0]>400 && prunedMassAK8[0]>50 && nAK8>=2 && @ptTopTagged.size()>0',
                    'xMin'   : '0',
                    'xMax'   : '4000',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/80GeV',
                    'log'    : True
                  },
               }

Cutflow_higgs_top = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*topSF(ptTopTagged)*btagsf',
                    'SigWts' : 'EvtWeight*EvtWtPV*topSF(ptTopTagged)*btagsf',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850&&ptAK8[0]>400 && prunedMassAK8[0]>50 && nAK8>=2 && isRegionD',
                    'xMin'   : '0',
                    'xMax'   : '4000',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/80GeV',
                    'log'    : True
                  },
             }
