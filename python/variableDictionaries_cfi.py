#!/usr/bin/env python
import ROOT as rt
sumPtDict = {
                '(ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
                    'Cuts'   : 'mtprimeDTilde_tM_H1M0L > (1000-1000*0.15) && mtprimeDTilde_tM_ZB < (1000+1000*0.15) && isRegionD_tM_ZB && @ptExtraAK4.size()>1 && (ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900 && !(higgsAnul[2])',
                    #'Cuts'   : '(ptAK8[0]+ptAK8[1])>850 && mtprimeDTilde_tM_H1M0L > (1000-1000*0.15) && mtprimeDTilde_tM_ZB < (1000+1000*0.15) && isRegionD_tM_ZB && @ptExtraAK4.size()>1 && (ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900 && !(higgsAnul[2])',
                    'xMin'   : '600',
                    'xMax'   : '3600',
                    'nBins'  : '100',
                    'xLabel' : 'Scalar Sum p_{T} of Leading 2 AK8 jets [GeV]',
                    'yLabel' : 'Events/20GeV',
                    'log'    : False
                  },
}
nBTags = {
                'dR(etaAK4,phiAK4,etaHTagged1M0L[0],phiHTagged1M0L[0])'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
                    'Cuts'   : 'isRegionB_tM_H1M0L&&(ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                    'xMin'   : '0', 
                    'xMax'   : '5', 
                    'nBins'  : '30',
                    'xLabel' : '#Delta R(AK4, H) region B [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : False
                  },
}
finalSel = {
#                'dR(etaAK4,phiAK4,etaHTagged1M0L[0],phiHTagged1M0L[0])'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : 'isRegionB_tM_H1M0L&&(ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
#                    'xMin'   : '0', 
#                    'xMax'   : '5', 
#                    'nBins'  : '30',
#                    'xLabel' : '#Delta R(AK4, H) region B [GeV]',
#                    'yLabel' : 'Jets',
#                    'log'    : False
#                  },
#                'max(sj0csvTopTaggedM,sj1csvTopTaggedM)'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '1',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '20',
#                    'xLabel' : 'Highest csvv2 discriminator, top tagged jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False 
#                  },
#                'max(sj0csvTopTagged0M,sj1csvTopTagged0M)'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '1',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '20',
#                    'xLabel' : 'Highest csvv2 discriminator, top tagged jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False 
#                  },
#                'abs(costheta(ptHTagged,etaHTagged,phiHTagged,MHTagged,ptTopTaggedM,etaTopTaggedM,phiTopTaggedM,MTopTaggedM))'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : 'isRegionD_tM',
#                    'xMin'   : '0',
#                    'xMax'   : '1',
#                    'nBins'  : '40',
#                    'xLabel' : 'Cos(#theta_{Tt}*)',
#                    'yLabel' : 'Events/0.1',
#                    'log'    : False
#                  },
#                '@ptExtraAK4.size()'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : 'isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850',
#                    'xMin'   : '-0.5', 
#                    'xMax'   : '10.5', 
#                    'nBins'  : '11',
#                    'xLabel' : 'N Extra AK4 Jets, Region B',
#                    'yLabel' : 'Jets',
#                    'log'    : False  
#                  },
#                'nAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : 'isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850',
#                    'xMin'   : '0', 
#                    'xMax'   : '10', 
#                    'nBins'  : '10',
#                    'xLabel' : 'nAK8 Jets, Region B',
#                    'yLabel' : 'Jets',
#                    'log'    : False
#                  },
#                'Sum$(abs(etaExtraAK4)>2.4)'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : 'isRegionD_tM',
#                    'xMin'   : '-0.5', 
#                    'xMax'   : '6.5', 
#                    'nBins'  : '7',
#                    'xLabel' : 'N Extra Forward AK4 Jets [GeV]',
#                    'yLabel' : 'Jets',
#                    'log'    : False                 
#                  },
##                'Sum$(abs(etaExtraAK4)>2.4)'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
##                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
##                    'Cuts'   : 'isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850',
##                    'xMin'   : '-0.5', 
##                    'xMax'   : '6.5', 
##                    'nBins'  : '7',
##                    'xLabel' : 'N Forward AK4 Jets, Region B [GeV]',
##                    'yLabel' : 'Jets',
##                    'log'    : False
##                  },
###                'Sum$(csvExtraAK4>0.8484)'
###                : {
###                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
###                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
###                    'Cuts'   : 'isRegionD_tM',
###                    'xMin'   : '-0.5', 
###                    'xMax'   : '6.5', 
###                    'nBins'  : '7',
###                    'xLabel' : 'N b-tagged Extra AK4 Jets [GeV]',
###                    'yLabel' : 'Jets',
###                    'log'    : False
###                  },
##                'Max$(abs(etaExtraAK4))'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
##                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
##                    'Cuts'   : 'isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850',
##                    'xMin'   : '0.', 
##                    'xMax'   : '5.', 
##                    'nBins'  : '25',
##                    'xLabel' : 'Maximum #eta Extra AK4 Jets, Region B',
##                    'yLabel' : 'Jets',
##                    'log'    : False
##                  },
##                'Max$(abs(etaAK4))'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
##                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
##                    'Cuts'   : 'isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850',
##                    'xMin'   : '0.', 
##                    'xMax'   : '5.', 
##                    'nBins'  : '25',
##                    'xLabel' : 'Maximum #eta AK4 Jets, Region B',
##                    'yLabel' : 'Jets',
##                    'log'    : False
##                  },
##                'etaExtraAK4'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
##                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
##                    'Cuts'   : 'isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850',
##                    'xMin'   : '-5.', 
##                    'xMax'   : '5.', 
##                    'nBins'  : '50',
##                    'xLabel' : '#eta Extra AK4 Jets, Region B',
##                    'yLabel' : 'Jets',
##                    'log'    : False
##                  },
##                'Max$(abs(etaAK4))'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
##                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
##                    'Cuts'   : 'isRegionD_tM && @ptExtraAK4.size()>1',
##                    'xMin'   : '0.', 
##                    'xMax'   : '5.', 
##                    'nBins'  : '25',
##                    'xLabel' : 'Maximum #eta AK4 Jets',
##                    'yLabel' : 'Jets',
##                    'log'    : False
##                  },
#                'ptAK4'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : 'isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1500.', 
#                    'nBins'  : '100',
#                    'xLabel' : 'p_{T} AK4 Jets, Region B [GeV]',
#                    'yLabel' : 'Jets/20 GeV',
#                    'log'    : False
#                  },
#                'etaAK4'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : 'isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850',
#                    'xMin'   : '-5.', 
#                    'xMax'   : '5.', 
#                    'nBins'  : '50',
#                    'xLabel' : '#eta AK4 Jets, Region B',
#                    'yLabel' : 'Jets',
#                    'log'    : False
#                  },
#                'ptAK8[0]'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850 && isRegionB_tM_H1M0L &&@ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
#                    'xMin'   : '200', 
#                    'xMax'   : '1500.', 
#                    'nBins'  : '37',
#                    'xLabel' : 'p_{T} leading AK8 Jet [GeV]',
#                    'yLabel' : 'Jets/35GeV',
#                    'log'    : False
#                  },
#                'ptAK8[1]'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850 && isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
#                    'xMin'   : '200', 
#                    'xMax'   : '1500.', 
#                    'nBins'  : '37',
#                    'xLabel' : 'p_{T} 2nd leading AK8 Jets [GeV]',
#                    'yLabel' : 'Jets/35GeV',
#                    'log'    : False
#                  },
##                'mtprimeDTilde_tM'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
##                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf',
##                    'Cuts'   : 'isRegionD_tM && @ptExtraAK4.size()>1 && (ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900',
##                    'xMin'   : '600', 
##                    'xMax'   : '3600.', 
##                    'nBins'  : '52',
##                    'xLabel' : '#tilde{M}(T) [GeV]',
##                    'yLabel' : 'Events',
##                    'log'    : False
##                  },
##                'ptAK8[0]+ptAK8[1]' 
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : 'isRegionD_tM',
#                    'xMin'   : '0',
#                    'xMax'   : '4000',
#                    'nBins'  : '200',
#                    'xLabel' : 'Scalar Sum p_{T} of Leading 2 AK8 jets [GeV]',
#                    'yLabel' : 'Events/20GeV',
#                    'log'    : False
#                  },
#                'tau3AK8/tau2AK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : 'isRegionD_tM_H1M0L',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '50',
#                    'xLabel' : '#tau_{32}, 2 leading AK8 jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False
#                  },
#                'max(sj0csvHTagged1M1L,sj1csvHTagged1M1L)'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : 'isRegionD_tM_H1M0L',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '20',
#                    'xLabel' : 'Highest csvv2 discriminator, higgs tagged jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False 
#                  },
#                'min(sj0csvHTagged1M1L,sj1csvHTagged1M1L)'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : 'isRegionD_tM_H1M0L',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '20',
#                    'xLabel' : 'lowest csvv2 discriminator, higgs tagged jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False 
#                  },
#                'PrunedMassAK8' 
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : 'isRegionB_tM_Zmass',
#                    'xMin'   : '0.',
#                    'xMax'   : '800.',
#                    'nBins'  : '40',
#                    'xLabel' : 'Pruned Mass, AK8 jets, region B [GeV]',
#                    'yLabel' : 'Jets/20 geV',
#                    'log'    : False
#                  },
#                'sj0CSVAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : 'PrunedMassAK8>105 && PrunedMassAK8<135 && tau2AK8/tau1AK8 < 0.6 && sj1CSVAK8>0.8484',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '20',
#                    'xLabel' : 'sj 0 csvv2 discriminator, H tagged jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False 
#                  },
#                'sj1CSVAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : 'PrunedMassAK8>105 && PrunedMassAK8<135 && tau2AK8/tau1AK8 < 0.6 && sj0CSVAK8>0.8484',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '20',
#                    'xLabel' : 'sj 0 csvv2 discriminator, H tagged jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False 
#                  },
#                'ptAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : 'isRegionD_tM',
#                    'xMin'   : '200', 
#                    'xMax'   : '3000.', 
#                    'nBins'  : '140',
#                    'xLabel' : 'p_{T} 2 leading AK8 Jets [GeV]',
#                    'yLabel' : 'Jets/20GeV',
#                    'log'    : False
#                  },
                'ptZTagged1M1L'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsf*btagsfMed*btagsfLoose*btagsfZ',
                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsf*btagsfMed*btagsfLoose*btagsfZ',
                    'Cuts'   : 'isRegionD_tM_ZB && (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                    'xMin'   : '200', 
                    'xMax'   : '2400', 
                    'nBins'  : '44',
                    'xLabel' : 'pt H Tagged Jets',
                    'yLabel' : 'Jets',
                    'log'    : False
                  },
#                '@ptTopTaggedM.size()'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : 'isRegionD_tM',
#                    'xMin'   : '-0.5', 
#                    'xMax'   : '10.5', 
#                    'nBins'  : '11',
#                    'xLabel' : 'n top Tagged Jets, 0.3% WP',
#                    'yLabel' : 'Jets',
#                    'log'    : False
#                  },
}
mtprimeTildes = {
#                'abs(costheta(ptHTagged1M1L,etaHTagged1M1L,phiHTagged1M1L,MHTagged1M1L,ptTopTagged0M,etaTopTagged0M,phiTopTagged0M,MTopTagged0M))'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'Cuts'   : 'isRegionC_tM_H1M0L',
#                    'xMin'   : '0',
#                    'xMax'   : '1',
#                    'nBins'  : '20',
#                    'xLabel' : 'Cos(#theta *)_{leading AK8 jets}',
#                    'yLabel' : 'Events/0.1',
#                    'log'    : False
#                  },
#                'Mjj(ptAK8[0],etaAK8[0],phiAK8[0],MAK8[0],ptAK8[1],etaAK8[1],phiAK8[1],MAK8[1])'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850 && PrunedMassAK8[0]>50 && ptAK8[0]>400',
#                    'xMin'   : '600', 
#                    'xMax'   : '2000.', 
#                    'nBins'  : '112',
#                    'xLabel' : 'Mjj [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                'mtprime'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850 && PrunedMassAK8[0]>50 && ptAK8[0]>400 && isRegionD && @ptExtraAK4.size()>1 && (ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900',
#                    'xMin'   : '600', 
#                    'xMax'   : '2000.', 
#                    'nBins'  : '28',
#                    'xLabel' : 'M_(T) [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                'mtprimeDTilde_tM_H1M0L'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                   'Cuts'   : 'isRegionD_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850 && !(higgsAnul[2])',
#                    'xMin'   : '600', 
#                    'xMax'   : '3600.', 
#                    'nBins'  : '25',
#                    'xLabel' : '#tilde{M}(T) [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                'mtprimeCTilde_tM_H1M0L'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                   'Cuts'   : 'isRegionC_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850 && !(higgsAnul[2])',
#                    'xMin'   : '600', 
#                    'xMax'   : '3600.', 
#                    'nBins'  : '25',
#                    'xLabel' : '#tilde{M}(T) [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                'mtprimeBTilde_tM_ZB'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
#                   #'Cuts'   : 'isRegionB_tM_ZB && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850',
#                   'Cuts'   : 'isRegionB_tM_ZB && (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && !(ZAnul[2])',
#                    'xMin'   : '600', 
#                    'xMax'   : '3100.', 
#                    'nBins'  : '50',
#                    'xLabel' : '#tilde{M}(T) [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                'mtprimeATilde_tM_H1M0L'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                   'Cuts'   : 'isRegionA_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850 && !(higgsAnul[2])',
#                    'xMin'   : '600', 
#                    'xMax'   : '3600.', 
#                    'nBins'  : '25',
#                    'xLabel' : '#tilde{M}(T) [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                'mtprimeDTilde_tM_ZB'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                   'Cuts'   : 'isRegionD_tM_ZB && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850 && !(ZAnul[2])',
#                    'xMin'   : '600', 
#                    'xMax'   : '3600.', 
#                    'nBins'  : '25',
#                    'xLabel' : '#tilde{M}(T) [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                'mtprimeCTilde_tM_ZB'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                   'Cuts'   : 'isRegionC_tM_ZB && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850 && !(ZAnul[2])',
#                    'xMin'   : '600', 
#                    'xMax'   : '3600.', 
#                    'nBins'  : '25',
#                    'xLabel' : '#tilde{M}(T) [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                'mtprimeBTilde_tM_ZB'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                   'Cuts'   : 'isRegionB_tM_ZB && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850 && !(ZAnul[2])',
#                    'xMin'   : '600', 
#                    'xMax'   : '3600.', 
#                    'nBins'  : '25',
#                    'xLabel' : '#tilde{M}(T) [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                'mtprimeATilde_tM_ZB'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                   'Cuts'   : 'isRegionA_tM_ZB && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850 && !(ZAnul[2])',
#                    'xMin'   : '600', 
#                    'xMax'   : '3600.', 
#                    'nBins'  : '25',
#                    'xLabel' : '#tilde{M}(T) [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
                'tH_RA_postfit'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                   'Cuts'   : 'isRegionB_tM_H1M0L && (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                    'xMin'   : '600', 
                    'xMax'   : '3100.', 
                    'nBins'  : '50',
                    'xLabel' : '#tilde{M}(T) [GeV]',
                    'yLabel' : 'Events',
                    'log'    : False
                  },
                'tH_RB_postfit'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                   'Cuts'   : 'isRegionB_tM_H1M0L && (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                    'xMin'   : '600', 
                    'xMax'   : '3100.', 
                    'nBins'  : '50',
                    'xLabel' : '#tilde{M}(T) [GeV]',
                    'yLabel' : 'Events',
                    'log'    : False
                  },
                'tH_RC_postfit'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                   'Cuts'   : 'isRegionB_tM_H1M0L && (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                    'xMin'   : '600', 
                    'xMax'   : '3100.', 
                    'nBins'  : '50',
                    'xLabel' : '#tilde{M}(T) [GeV]',
                    'yLabel' : 'Events',
                    'log'    : False
                  },
                'tH_RD_postfit'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                   'Cuts'   : 'isRegionB_tM_H1M0L && (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                    'xMin'   : '600', 
                    'xMax'   : '3100.', 
                    'nBins'  : '50',
                    'xLabel' : '#tilde{M}(T) [GeV]',
                    'yLabel' : 'Events',
                    'log'    : False
                  },
                'tZ_RA_postfit'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                   'Cuts'   : 'isRegionB_tM_H1M0L && (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                    'xMin'   : '600', 
                    'xMax'   : '3100.', 
                    'nBins'  : '50',
                    'xLabel' : '#tilde{M}(T) [GeV]',
                    'yLabel' : 'Events',
                    'log'    : False
                  },
                'tZ_RB_postfit'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                   'Cuts'   : 'isRegionB_tM_H1M0L && (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                    'xMin'   : '600', 
                    'xMax'   : '3100.', 
                    'nBins'  : '50',
                    'xLabel' : '#tilde{M}(T) [GeV]',
                    'yLabel' : 'Events',
                    'log'    : False
                  },
                'tZ_RC_postfit'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                   'Cuts'   : 'isRegionB_tM_H1M0L && (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                    'xMin'   : '600', 
                    'xMax'   : '3100.', 
                    'nBins'  : '50',
                    'xLabel' : '#tilde{M}(T) [GeV]',
                    'yLabel' : 'Events',
                    'log'    : False
                  },
                'tZ_RD_postfit'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                   'Cuts'   : 'isRegionB_tM_H1M0L && (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                    'xMin'   : '600', 
                    'xMax'   : '3100.', 
                    'nBins'  : '50',
                    'xLabel' : '#tilde{M}(T) [GeV]',
                    'yLabel' : 'Events',
                    'log'    : False
                  },
#                'MTP_regionB'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
#                   #'Cuts'   : 'isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850',
#                   'Cuts'   : 'isRegionB_tM_H1M0L && (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
#                    'xMin'   : '600', 
#                    'xMax'   : '3100.', 
#                    'nBins'  : '25',
#                    'xLabel' : '#tilde{M}(T) region B [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                'MTP_regionC'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
#                   #'Cuts'   : 'isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850',
#                   'Cuts'   : 'isRegionB_tM_H1M0L && (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
#                    'xMin'   : '600', 
#                    'xMax'   : '3100.', 
#                    'nBins'  : '25',
#                    'xLabel' : '#tilde{M}(T) region C [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                'MTP_regionD'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
#                   #'Cuts'   : 'isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850',
#                   'Cuts'   : 'isRegionB_tM_H1M0L && (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
#                    'xMin'   : '600', 
#                    'xMax'   : '3100.', 
#                    'nBins'  : '25',
#                    'xLabel' : '#tilde{M}(T) region D [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                'MTP'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
#                   #'Cuts'   : 'isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850',
#                   'Cuts'   : 'isRegionB_tM_H1M0L && (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
#                    'xMin'   : '600', 
#                    'xMax'   : '3100.', 
#                    'nBins'  : '25',
#                    'xLabel' : '#tilde{M}(T) [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                'ptAK4[0]'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
#                   'Cuts'   : 'isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && (ptAK8[0]+ptAK8[1])>850',# && !(ZAnul[2])',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1500.', 
#                    'nBins'  : '50',
#                    'xLabel' : 'pt leading AK4 [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
           }
forwardJets = {
                'Max$(abs(etaAK4))'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
                    'Cuts'   : '1 && isRegionD',
                    'xMin'   : '0.', 
                    'xMax'   : '5.', 
                    'nBins'  : '25',
                    'xLabel' : 'Maximum #eta AK4 Jets [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : False
                  },
             }
nTop = {
                'ptHTagged'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts'    : 'EvtWeight*EvtWtPV',
                    'Cuts'   : 'sj0CSVHTagged>0.8484 && !(sj1CSVHTagged>0.8484)',
                    'xMin'   : '200', 
                    'xMax'   : '3000', 
                    'nBins'  : '100',
                    'xLabel' : 'n top tagged Jets [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : False
                  },
#                'ptHTagged1M1L'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : 'sj0csvHTagged1M1L>0.8484 && sj1csvHTagged1M1L>0.8484',
#                    'xMin'   : '200', 
#                    'xMax'   : '3000', 
#                    'nBins'  : '100',
#                    'xLabel' : 'n top tagged Jets [GeV]',
#                    'yLabel' : 'Jets',
#                    'log'    : False
#                  },
      }
ptAK8 = {
#                'mtprimeTilde(mtprime,MTopTagged[0],MHTagged[0])'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                   'Cuts'   : '1 && isRegionD',
#                    'xMin'   : '600', 
#                    'xMax'   : '3600.', 
#                    'nBins'  : '52',
#                    'xLabel' : '#tilde{M}(T) [GeV]',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
                'sj0ptAK8[0]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*btagsf*btagsfLoose*btagsfMed*btagsfZ*toptagsf',
                    'SigWts'    : 'EvtWeight*EvtWtPV*btagsf*btagsfLoose*btagsfMed*btagsfZ*toptagsf',
                    'Cuts'   : 'isRegionA_tM_H1M0L && Sum$(abs(etaAK4)>2.4)==0 && (ptAK8[0]+ptAK8[1])>850 && ptAK8[0]>400 && tau3AK8[0]/tau2AK8[0]<0.57',
                    'xMin'   : '0', 
                    'xMax'   : '600', 
                    'nBins'  : '50',
                    'xLabel' : 'pt SJ 0, leading AK8 [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : False
                  },
                'sj1ptAK8[0]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*btagsf*btagsfLoose*btagsfMed*btagsfZ*toptagsf',
                    'SigWts'    : 'EvtWeight*EvtWtPV*btagsf*btagsfLoose*btagsfMed*btagsfZ*toptagsf',
                    'Cuts'   : 'isRegionA_tM_H1M0L && Sum$(abs(etaAK4)>2.4)==0 && (ptAK8[0]+ptAK8[1])>850 && ptAK8[0]>400 && tau3AK8[0]/tau2AK8[0]<0.57',
                    'xMin'   : '0', 
                    'xMax'   : '600', 
                    'nBins'  : '50',
                    'xLabel' : 'pt SJ 1, leading AK8 [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : False
                  },
                'sj0ptAK8[1]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*btagsf*btagsfLoose*btagsfMed*btagsfZ*toptagsf',
                    'SigWts'    : 'EvtWeight*EvtWtPV*btagsf*btagsfLoose*btagsfMed*btagsfZ*toptagsf',
                    'Cuts'   : 'isRegionA_tM_H1M0L &&  Sum$(abs(etaAK4)>2.4)==0 && (ptAK8[0]+ptAK8[1])>850 && ptAK8[1]>400 && tau3AK8[1]/tau2AK8[1]<0.57',
                    'xMin'   : '0', 
                    'xMax'   : '600', 
                    'nBins'  : '50',
                    'xLabel' : 'pt SJ 0, leading AK8 [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : False
                  },
                'sj1ptAK8[1]'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*btagsf*btagsfLoose*btagsfMed*btagsfZ*toptagsf',
                    'SigWts'    : 'EvtWeight*EvtWtPV*btagsf*btagsfLoose*btagsfMed*btagsfZ*toptagsf',
                    'Cuts'   : 'isRegionA_tM_H1M0L && Sum$(abs(etaAK4)>2.4)==0 && (ptAK8[0]+ptAK8[1])>850 && ptAK8[1]>400 && tau3AK8[1]/tau2AK8[1]<0.57',
                    'xMin'   : '0', 
                    'xMax'   : '600', 
                    'nBins'  : '50',
                    'xLabel' : 'pt SJ 1, leading AK8 [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : False
                  },
#                'ptHTagged'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '1 && isRegionD',
#                    'xMin'   : '200', 
#                    'xMax'   : '3000.', 
#                    'nBins'  : '140',
#                    'xLabel' : 'p_{T} AK8 Jets [GeV]',
#                    'yLabel' : 'Jets/20GeV',
#                    'log'    : False
#                  },
}
preselDict = {
#                'npv' 
#                : {
#                    #'Wts'    : 'EvtWeight*(EvtWtPVBG*27259+EvtWtPVH*8605.689)/35865.177',
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsf*btagsfMed*btagsfLoose*btagsfZ',
#                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsf*btagsfMed*btagsfLoose*btagsfZ',
#                    'Cuts'   : '1',
#                    'xMin'   : '0.',
#                    'xMax'   : '50.',
#                    'nBins'  : '50',
#                    'xLabel' : 'nPV',
#                    'yLabel' : 'Events',
#                    'log'    : False
#                  },
#                '@ptExtraAK4.size()'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'Cuts'   : '1',
#                    'xMin'   : '-0.5', 
#                    'xMax'   : '6.5', 
#                    'nBins'  : '7',
#                    'xLabel' : 'N Extra AK4 Jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False  
#                  },
#                'Max$(abs(etaExtraAK4))'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsf*btagsfMed*btagsfLoose*btagsfZ',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsf*btagsfMed*btagsfLoose*btagsfZ',
#                    'Cuts'   : '@ptExtraAK4.size()>1 && isRegionD_tM_H1M0L',
#                    'xMin'   : '0.', 
#                    'xMax'   : '5.', 
#                    'nBins'  : '25',
#                    'xLabel' : 'Maximum #eta Extra AK4 Jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False
#                  },
                'ptAK8[0]+ptAK8[1]' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    #'Cuts'   : 'SelectedEvent_hltdecision && SelectedEvent_hltdecisionBG',
                    'Cuts'   : 'SelectedEvent_hltdecisionBG',
                    'xMin'   : '0',
                    'xMax'   : '2000',
                    'nBins'  : '40',
                    'xLabel' : 'Scalar Sum p_{T} of Leading 2 AK8 jets [GeV]',
                    'yLabel' : 'Events/20GeV',
                    'log'    : False
                  },
#                'ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1]' 
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '@ptExtraAK4.size()>1',
#                    'xMin'   : '0',
#                    'xMax'   : '4000',
#                    'nBins'  : '200',
#                    'xLabel' : 'Scalar Sum p_{T} of Leading 2 AK8 jets [GeV]',
#                    'yLabel' : 'Events/20GeV',
#                    'log'    : False
#                  },
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    #'Cuts'   : 'SelectedEvent_hltdecision && SelectedEvent_hltdecisionBG',
                    'Cuts'   : 'SelectedEvent_hltdecisionBG',
                    'xMin'   : '500',
                    'xMax'   : '3000.',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/50GeV',
                    'log'    : False
                  },
                'etaAK8'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    #'Cuts'   : 'SelectedEvent_hltdecision && SelectedEvent_hltdecisionBG',
                    'Cuts'   : 'SelectedEvent_hltdecisionBG',
                    'xMin'   : '-5.', 
                    'xMax'   : '5.', 
                    'nBins'  : '50',
                    'xLabel' : '#eta 2 leading AK8 Jets',
                    'yLabel' : 'Jets',
                    'log'    : False
                  },
                'phiAK8'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    #'Cuts'   : 'SelectedEvent_hltdecision && SelectedEvent_hltdecisionBG',
                    'Cuts'   : 'SelectedEvent_hltdecisionBG',
                    'xMin'   : '-5.', 
                    'xMax'   : '5.', 
                    'nBins'  : '50',
                    'xLabel' : '#eta 2 leading AK8 Jets',
                    'yLabel' : 'Jets',
                    'log'    : False
                  },
                'abs(etaAK4)'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    #'Cuts'   : 'SelectedEvent_hltdecision && SelectedEvent_hltdecisionBG && abs(etaAK4)>2.4',
                    'Cuts'   : 'SelectedEvent_hltdecisionBG && abs(etaAK4)>2.4',
                    'xMin'   : '-5.', 
                    'xMax'   : '5.', 
                    'nBins'  : '50',
                    'xLabel' : '#eta 2 leading AK8 Jets',
                    'yLabel' : 'Jets',
                    'log'    : False
                  },
                'phiAK4'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    #'Cuts'   : 'SelectedEvent_hltdecision && SelectedEvent_hltdecisionBG && abs(etaAK4)>2.4',
                    'Cuts'   : 'SelectedEvent_hltdecisionBG && abs(etaAK4)>2.4',
                    'xMin'   : '-5.', 
                    'xMax'   : '5.', 
                    'nBins'  : '50',
                    'xLabel' : '#eta 2 leading AK8 Jets',
                    'yLabel' : 'Jets',
                    'log'    : False
                  },
#                'ptAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1]) && (ptAK8[0]+ptAK8[1])>850',
#                    'xMin'   : '200', 
#                    'xMax'   : '3000.', 
#                    'nBins'  : '140',
#                    'xLabel' : 'p_{T} 2 leading AK8 Jets [GeV]',
#                    'yLabel' : 'Jets/20GeV',
#                    'log'    : False
#                  },
#                'ptAK8[0]'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850',
#                    'xMin'   : '200', 
#                    'xMax'   : '3000', 
#                    'nBins'  : '140',
#                    'xLabel' : 'p_{T} leading AK8 Jet [GeV]',
#                    'yLabel' : 'Jets/35GeV',
#                    'log'    : False
#                  },
#                'ptAK8[1]'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850 && isRegionA_tM_H1M0L',
#                    'xMin'   : '200', 
#                    'xMax'   : '1500.', 
#                    'nBins'  : '37',
#                    'xLabel' : 'p_{T} 2nd leading AK8 Jets [GeV]',
#                    'yLabel' : 'Jets/35GeV',
#                    'log'    : False
#                  },
#                'etaAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&& (ptAK8[0]+ptAK8[1])>850',
#                    'xMin'   : '-5.', 
#                    'xMax'   : '5.', 
#                    'nBins'  : '50',
#                    'xLabel' : '#eta 2 leading AK8 Jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False
#                  },
#                'PrunedMassAK8' 
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&& (ptAK8[0]+ptAK8[1])>850',
#                    'xMin'   : '0.',
#                    'xMax'   : '800.',
#                    'nBins'  : '40',
#                    'xLabel' : 'Pruned Mass, 2 leading AK8 jets [GeV]',
#                    'yLabel' : 'Jets/20 geV',
#                    'log'    : False
#                  },
#                'SoftDropMassAK8' 
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts' : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&& (ptAK8[0]+ptAK8[1])>850',
#                    'xMin'   : '0.',
#                    'xMax'   : '800.',
#                    'nBins'  : '40',
#                    'xLabel' : 'Soft Drop Mass, 2 leading AK8 jets [GeV]',
#                    'yLabel' : 'Jets/20 GeV',
#                    'log'    : False
#                  },
##                'tau2AK8/tau1AK8'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV',
##                    'SigWts' : 'EvtWeight*EvtWtPV',
##                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&& (ptAK8[0]+ptAK8[1])>850',
##                    'xMin'   : '0.', 
##                    'xMax'   : '1.', 
##                    'nBins'  : '50',
##                    'xLabel' : '#tau_{21}, 2 leading AK8 jets',
##                    'yLabel' : 'Jets',
##                    'log'    : False 
##                  },
##                 'tau3AK8/tau2AK8'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV',
##                    'SigWts' : 'EvtWeight*EvtWtPV',
##                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&& (ptAK8[0]+ptAK8[1])>850',
##                    'xMin'   : '0.', 
##                    'xMax'   : '1.', 
##                    'nBins'  : '50',
##                    'xLabel' : '#tau_{32}, 2 leading AK8 jets',
##                    'yLabel' : 'Jets',
##                    'log'    : False
##                  },
###                'max(sj0CSVAK8,sj1CSVAK8)'
###                : {
###                    'Wts'    : 'EvtWeight*EvtWtPV',
###                    'SigWts' : 'EvtWeight*EvtWtPV',
###                    #'Wts'    : 'EvtWeight*EvtWtPV',
###                    #'SigWts'    : 'EvtWeight*EvtWtPV',
###                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&& (ptAK8[0]+ptAK8[1])>850',
###                    #'Cuts'   : '1 && @idxHTagged.size()>0 && idxAK8 != idxHTagged',
###                    'xMin'   : '0.', 
###                    'xMax'   : '1.', 
###                    'nBins'  : '20',
###                    'xLabel' : 'Highest CSVv2 discriminator, 2 leading AK8 jet',
###                    'yLabel' : 'Jets',
###                    'log'    : False
###                  },
#                'sj0CSVAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&& (ptAK8[0]+ptAK8[1])>850',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '20',
#                    'xLabel' : 'subjet 0 CSVv2 discriminator, 2 leading AK8 jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False
#                  },
#                'sj1CSVAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(idxAK8==idxAK8[0]||idxAK8==idxAK8[1])&& (ptAK8[0]+ptAK8[1])>850',
#                    'xMin'   : '0.', 
#                    'xMax'   : '1.', 
#                    'nBins'  : '20',
#                    'xLabel' : 'subjet 1 CSVv2 discriminator, 2 leading AK8 jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False
#                  },
#                'ptAK4'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
#                    'xMin'   : '0.', 
#                    'xMax'   : '2000.', 
#                    'nBins'  : '100',
#                    'xLabel' : 'p_{T} AK4 Jets [GeV]',
#                    'yLabel' : 'Jets/20 GeV',
#                    'log'    : False
#                  },
#                'etaAK4'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850',
#                    'xMin'   : '-5.', 
#                    'xMax'   : '5.', 
#                    'nBins'  : '50',
#                    'xLabel' : '#eta AK4 Jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False
#                  },
#                'nAK4'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV',
#                    'SigWts'    : 'EvtWeight*EvtWtPV',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850',
#                    'xMin'   : '0', 
#                    'xMax'   : '25', 
#                    'nBins'  : '25',
#                    'xLabel' : 'nAK4 Jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False
#                  },
#                'nAK8'
#                : {
#                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'SigWts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed',
#                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850',
#                    'xMin'   : '0', 
#                    'xMax'   : '10', 
#                    'nBins'  : '10',
#                    'xLabel' : 'nAK8 Jets',
#                    'yLabel' : 'Jets',
#                    'log'    : False
#                  },
##                '@idxHTagged.size()'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV',
##                    'SigWts'    : 'EvtWeight*EvtWtPV',
##                    'Cuts'   : '1',
##                    'xMin'   : '0', 
##                    'xMax'   : '8', 
##                    'nBins'  : '8',
##                    'xLabel' : 'n Higgs tagged Jets [GeV]',
##                    'yLabel' : 'Jets',
##                    'log'    : False
##                  },
##                '@idxTopTagged.size()'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV*topSF(ptAK8)',
##                    'SigWts'    : 'EvtWeight*EvtWtPV*topSF(ptAK8)',
##                    'Cuts'   : '1',
##                    'xMin'   : '0', 
##                    'xMax'   : '8', 
##                    'nBins'  : '8',
##                    'xLabel' : 'n top tagged Jets [GeV]',
##                    'yLabel' : 'Jets',
##                    'log'    : False
##                  },
##                '@idxZTagged.size()'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV',
##                    'SigWts'    : 'EvtWeight*EvtWtPV',
##                    'Cuts'   : '1',
##                    'xMin'   : '0', 
##                    'xMax'   : '8', 
##                    'nBins'  : '8',
##                    'xLabel' : 'n Z tagged Jets [GeV]',
##                    'yLabel' : 'Jets',
##                    'log'    : False
##                  },
##		'costheta(ptAK8[idxAK8[0]],etaAK8[idxAK8[0]],phiAK8[idxAK8[0]],MAK8[idxAK8[0]],ptAK8[idxAK8[1]],etaAK8[idxAK8[1]],phiAK8[idxAK8[1]],MAK8[idxAK8[1]])'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV',
##                    'SigWts' : 'EvtWeight*EvtWtPV',
##                    'Cuts'   : '1',
##                    'xMin'   : '-1',
##                    'xMax'   : '1',
##                    'nBins'  : '20',
##                    'xLabel' : 'Cos(#theta *)_{leading AK8 jets}',
##                    'yLabel' : 'Events/0.1',
##                    'log'    : False
##                  },
##                'gammabeta(ptAK8[idxAK8[0]],etaAK8[idxAK8[0]],phiAK8[idxAK8[0]],MAK8[idxAK8[0]],ptAK8[idxAK8[1]],etaAK8[idxAK8[1]],phiAK8[idxAK8[1]],MAK8[idxAK8[1]])'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV',
##                    'SigWts' : 'EvtWeight*EvtWtPV',
##                    'Cuts'   : '1',
##                    'xMin'   : '0',
##                    'xMax'   : '5',
##                    'nBins'  : '50',
##                    'xLabel' : '#gamma#beta_{2 leading AK8 jets}',
##                    'yLabel' : 'Events/0.2',
##                    'log'    : False
##		},
##		'cos(delPhi(ptAK8[idxAK8[0]],etaAK8[idxAK8[0]],phiAK8[idxAK8[0]],MAK8[idxAK8[0]],ptAK8[idxAK8[1]],etaAK8[idxAK8[1]],phiAK8[idxAK8[1]],MAK8[idxAK8[1]]))'
##                : { 
##                    'Wts'    : 'EvtWeight*EvtWtPV',
##                    'SigWts' : 'EvtWeight*EvtWtPV',
##                    'Cuts'   : '1',
##                    'xMin'   : '-1',
##                    'xMax'   : '1',
##                    'nBins'  : '25',
##                    'xLabel' : 'Cos(#Delta#phi_{leading AK8 jets}',
##                    'yLabel' : 'Events',
##                    'log'    : False
##                  } ,
##		'delEta(etaAK8[idxAK8[0]],etaAK8[idxAK8[1]])'
##                : { 
##                    'Wts'    : 'EvtWeight*EvtWtPV',
##                    'SigWts' : 'EvtWeight*EvtWtPV',
##                    'Cuts'   : '1',
##                    'xMin'   : '-5',
##                    'xMax'   : '5',
##                    'nBins'  : '50',
##                    'xLabel' : '#Delta#eta_{leading AK8 jets}',
##                    'yLabel' : 'Events/0.2',
##                    'log'    : False
##                  } ,
##                'dR(etaAK8[0],phiAK8[0],etaAK8[1],phiAK8[1])'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV',
##                    'SigWts' : 'EvtWeight*EvtWtPV',
##                    'Cuts'   : '1',
##                    'xMin'   : '0',
##                    'xMax'   : '7',
##                    'nBins'  : '35',
##                    'xLabel' : '#DeltaR_{leading AK8 jets}',
##                    'yLabel' : 'Events',
##                    'log'    : False
##                  } ,
##                'Mjj(ptAK8[idxAK8[0]],etaAK8[idxAK8[0]],phiAK8[idxAK8[0]],MAK8[idxAK8[0]],ptAK8[idxAK8[1]],etaAK8[idxAK8[1]],phiAK8[idxAK8[1]],MAK8[idxAK8[1]])'
##                : {
##                    'Wts'    : 'EvtWeight*EvtWtPV',
##                    'SigWts' : 'EvtWeight*EvtWtPV',
##                    'Cuts'   : '1',
##                    'xMin'   : '850',
##                    'xMax'   : '4000',
##                    'nBins'  : '63',
##                    'xLabel' : 'M_{jj} [GeV]',
##                    'yLabel' : 'Events/50 GeV',
##                    'log'    : False
##                  } ,
  
             }

Cutflow_pre = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850',
                    'xMin'   : '0',
                    'xMax'   : '4000',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/80GeV',
                    'log'    : False
                  },
             }
Cutflow_init = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850 && isRegionD_tM_ZB',
                    'xMin'   : '0',
                    'xMax'   : '4000',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/80GeV',
                    'log'    : False
                  },
             }
Cutflow_extra = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850 && isRegionD_tM_ZB && @ptExtraAK4.size()>1',
                    'xMin'   : '0',
                    'xMax'   : '4000',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/80GeV',
                    'log'    : False
                  },
             }
Cutflow_forward = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850 && isRegionD_tM_ZB && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                    'xMin'   : '0',
                    'xMax'   : '4000',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/80GeV',
                    'log'    : False
                  },
             }
Cutflow_annulus = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                    'Cuts'   : '(ptAK8[0]+ptAK8[1])>850 && isRegionD_tM_ZB && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && !(ZAnul[2])',
                    'xMin'   : '0',
                    'xMax'   : '4000',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/80GeV',
                    'log'    : False
                  }, #
             }       #
                     #
                     #
                     #
                     #
                     #
                     #
                     #
                     #
                     #
