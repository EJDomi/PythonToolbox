# Dictionaries containing variable parameters for ABCD regions and systematics
isRegionA_mt = {
              'mtprimeATilde_tM_H1M0L' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_topSFUp'   : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_topSFDown'   : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_bcUp'   : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsfZ_bcUp*btagsf_bcUp*toptagsf',
                       'Wts_bcDown'   : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsfZ_bcDown*btagsf_bcDown*toptagsf',
                       'Wts_lUp'   : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsfZ_lUp*btagsf_lUp*toptagsf',
                       'Wts_lDown'   : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsfZ_lDown*btagsf_lDown*toptagsf',
                       'Wts_HTUp'   : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,1)*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_HTDown'   : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,-1)*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_topSFUp' : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_topSFDown' : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_bcUp'   : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsfZ_bcUp*btagsf_bcUp*toptagsf',
                       'SigWts_bcDown'   : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsfZ_bcDown*btagsf_bcDown*toptagsf',
                       'SigWts_lUp'   : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsfZ_lUp*btagsf_lUp*toptagsf',
                       'SigWts_lDown'   : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsfZ_lDown*btagsf_lDown*toptagsf',
                       'SigWts_HTUp'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_HTDown'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       #'Cuts'  : ' ptAK8[idxAK8[0]]>500 && ptAK8[idxAK8[1]]>300 && (idxAK8 == idxAK8[0] || idxAK8 == idxAK8[1]) && ht>1100&&(@idxHTagged.size()==0&&@idxAntiHTagged.size()>0&&@idxTopTagged.size()==0)&&Max$(abs(etaAK4))>1.5',
                       #'Cuts'  : ' ptAK8[idxAK8[0]]>400 && ptAK8[idxAK8[1]]>200 && (idxAK8[0] == idxAntiHTagged || idxAK8[1] == idxAntiHTagged) && ht>1100 && isRegionA && ptAntiHTagged > 300',
                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850&&ptAK8[idxAK8[0]]>400&&PrunedMassAK8[idxAK8[0]]>50&&isRegionA',
#                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&  ptAK8[idxAK8[0]]>500 && PrunedMassAK8[idxAK8[0]]>50 && isRegionA && ptAntiHTagged>500 && ptAntiTopTagged>500',
                       #'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&  ptAK8[idxAK8[0]]>400 && PrunedMassAK8[idxAK8[0]]>50 && @idxAntiTopTagged.size()>0 && @idxAntiHTagged.size()>0 && @idxTopTagged.size()==0 && @idxHTagged.size()==0',
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '25',
                       'xLabel' : 'M_{T} [GeV]',
                       'yLabel' : 'Events/50GeV',
                       'log'   : True
                     }
            }
isRegionB_mt = {
              'mtprimeBTilde_tM_H1M0L' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_topSFUp'   : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_topSFDown'   : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_bcUp'   : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsfZ_bcUp*btagsf_bcUp*toptagsf',
                       'Wts_bcDown'   : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsfZ_bcDown*btagsf_bcDown*toptagsf',
                       'Wts_lUp'   : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsfZ_lUp*btagsf_lUp*toptagsf',
                       'Wts_lDown'   : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsfZ_lDown*btagsf_lDown*toptagsf',
                       'Wts_HTUp'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ*QuadWeightHT(ht,1)',
                       'Wts_HTDown'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ*QuadWeightHT(ht,-1)',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_topSFUp'   : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_topSFDown'   : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_bcUp' : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsfZ_bcUp*btagsf_bcUp*toptagsf',
                       'SigWts_bcDown' : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsfZ_bcDown*btagsf_bcDown*toptagsf',
                       'SigWts_lUp' : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsfZ_lUp*btagsf_lUp*toptagsf',
                       'SigWts_lDown' : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsfZ_lDown*btagsf_lDown*toptagsf',
                       'SigWts_HTUp'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_HTDown'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       #'Cuts'  : ' ptAK8[idxAK8[0]]>400 && ptAK8[idxAK8[1]]>300 && (idxAK8[0] == idxAntiHTagged && idxAK8[1] == idxTopTagged) || (idxAK8[1] == idxAntiHTagged && idxAK8[0] == idxTopTagged) && ht>1100&&isRegionB && ptAntiHTagged > 300',
#                       'Cuts'  : ' ptAK8[idxAK8[0]]>400 && ptAK8[idxAK8[1]]>200 && @idxHTagged.size()==0 && @idxAntiHTagged.size()>0 && @idxTopTagged.size()>0 && ptTopTagged>400&&(tau3TopTagged/tau2TopTagged)<0.5&&SoftDropMassTopTagged<220&&SoftDropMassTopTagged>=105&&max(sj0CSVTopTagged,sj1CSVTopTagged)>=0.460 && dR(etaAntiHTagged,phiAntiHTagged,etaTopTagged,phiTopTagged)>2.0',
                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850&&ptAK8[idxAK8[0]]>400&&PrunedMassAK8[idxAK8[0]]>50&&isRegionB',
#                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&  ptAK8[idxAK8[0]]>500 && PrunedMassAK8[idxAK8[0]]>50 && isRegionB && ptAntiHTagged>500 && ptTopTagged>500',
#                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&  ptAK8[idxAK8[0]]>400 && PrunedMassAK8[idxAK8[0]]>50 && @idxAntiHTagged.size()>0 && @idxTopTagged.size()>0 && @idxHTagged.size()==0',
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '25',
                       'xLabel' : 'M_{T} [GeV]',
                       'yLabel' : 'Events/50GeV',
                       'log'   : True
                     }
            }
isRegionC_mt = {
              'mtprimeCTilde_tM_H1M0L' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_topSFUp'   : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_topSFDown'   : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_bcUp'   : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsfZ_bcUp*btagsf_bcUp*toptagsf',
                       'Wts_bcDown'   : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsfZ_bcDown*btagsf_bcDown*toptagsf',
                       'Wts_lUp'   : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsfZ_lUp*btagsf_lUp*toptagsf',
                       'Wts_lDown'   : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsfZ_lDown*btagsf_lDown*toptagsf',
                       'Wts_HTUp'   : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,1)*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_HTDown'   : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,-1)*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_topSFUp'   : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_topSFDown'   : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_bcUp'   : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsfZ_bcUp*btagsf_bcUp*toptagsf',
                       'SigWts_bcDown'   : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsfZ_bcDown*btagsf_bcDown*toptagsf',
                       'SigWts_lUp'   : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsfZ_lUp*btagsf_lUp*toptagsf',
                       'SigWts_lDown'   : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsfZ_lDown*btagsf_lDown*toptagsf',
                       'SigWts_HTUp'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_HTDown'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       #'Cuts'  : ' ptAK8[idxAK8[0]]>500 && ptAK8[idxAK8[1]]>300 && (idxAK8 == idxAK8[0] || idxAK8 == idxAK8[1]) && ht>1100&&(@idxHTagged.size()>0&&@idxAntiHTagged.size()>=0&&@idxTopTagged.size()==0)&&isRegionC&&Max$(abs(etaAK4))>1.5',
                       #'Cuts'  : ' ptAK8[idxAK8[0]]>400 && ptAK8[idxAK8[1]]>300 && (idxAK8[0] == idxHTagged || idxAK8[1] == idxHTagged)  && ht>1100&&isRegionC ',
#                       'Cuts'  : ' ptAK8[idxAK8[0]]>400 && ptAK8[idxAK8[1]]>200 && @idxHTagged.size()>0 && @idxAntiHTagged.size()>=0 && @idxTopTagged.size()>0 && ptTopTagged>400&&(tau3TopTagged/tau2TopTagged)<0.5&&SoftDropMassTopTagged<220&&SoftDropMassTopTagged>=105&&max(sj0CSVTopTagged,sj1CSVTopTagged)<0.460 && dR(etaHTagged,phiHTagged,etaTopTagged,phiTopTagged)>2.0',
                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850&&ptAK8[idxAK8[0]]>400&&PrunedMassAK8[idxAK8[0]]>50&&isRegionC',
#                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&  ptAK8[idxAK8[0]]>500 && PrunedMassAK8[idxAK8[0]]>50 && isRegionC && ptHTagged>500 && ptAntiTopTagged>500',
#                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&  ptAK8[idxAK8[0]]>400 && PrunedMassAK8[idxAK8[0]]>50 && @idxHTagged.size()>0 && @idxAntiTopTagged.size()>0 && @idxTopTagged.size()==0',
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '25',
                       'xLabel' : 'M_{T} [GeV]',
                       'yLabel' : 'Events/50GeV',
                       'log'   : True
                     }
            }
isRegionD_mt = {
              'mtprimeDTilde_tM_H1M0L' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_HTUp'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ*QuadWeightHT(ht,1)',
                       'Wts_HTDown'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ*QuadWeightHT(ht,-1)',
                       'Wts_bcUp'   : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsfZ_bcUp*btagsf_bcUp*toptagsf',
                       'Wts_bcDown'   : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsfZ_bcDown*btagsf_bcDown*toptagsf',
                       'Wts_lUp'   : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsfZ_lUp*btagsf_lUp*toptagsf',
                       'Wts_lDown'   : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsfZ_lDown*btagsf_lDown*toptagsf',
                       'Wts_topSFUp'   : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_topSFDown'   : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_HTUp'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_HTDown'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_bcUp'   : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsfZ_bcUp*btagsf_bcUp*toptagsf',
                       'SigWts_bcDown'   : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsfZ_bcDown*btagsf_bcDown*toptagsf',
                       'SigWts_lUp'   : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsfZ_lUp*btagsf_lUp*toptagsf',
                       'SigWts_lDown'   : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsfZ_lDown*btagsf_lDown*toptagsf',
                       'SigWts_topSFUp'   : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_topSFDown'   : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
#                       'Cuts'  : ' ptAK8[idxAK8[0]]>400 && ptAK8[idxAK8[1]]>300 && @idxHTagged.size()>0 && @idxAntiHTagged.size()>=0 && @idxTopTagged.size()>0 && ptTopTagged>400&&(tau3TopTagged/tau2TopTagged)<0.5&&SoftDropMassTopTagged<220&&SoftDropMassTopTagged>=105&&max(sj0CSVTopTagged,sj1CSVTopTagged)>=0.460 && dR(etaHTagged,phiHTagged,etaTopTagged,phiTopTagged)>2.0 ',
                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850&&ptAK8[idxAK8[0]]>400&&PrunedMassAK8[idxAK8[0]]>50&&isRegionD',
#                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&   ptAK8[idxAK8[0]]>500 && PrunedMassAK8[idxAK8[0]]>50 && isRegionD && ptHTagged>500 && ptTopTagged>500',
#                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&   ptAK8[idxAK8[0]]>400 && PrunedMassAK8[idxAK8[0]]>50 && @idxHTagged.size()>0 && @idxTopTagged.size()>0',
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '25',
                       'xLabel' : 'M_{T} [GeV]',
                       'yLabel' : 'Events/50GeV',
                       'log'   : True
                     }
               }
isRegionA_mt_tZ = {
              'mtprimeATilde_tM_ZB' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_topSFUp'   : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_topSFDown'   : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_bcUp'   : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsf_bcUp*btagsfZ_bcUp*toptagsf',
                       'Wts_bcDown'   : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsf_bcDown*btagsfZ_bcDown*toptagsf',
                       'Wts_lUp'   : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsf_lUp*btagsfZ_lUp*toptagsf',
                       'Wts_lDown'   : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsf_lDown*btagsfZ_lDown*toptagsf',
                       'Wts_HTUp'   : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,1)*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_HTDown'   : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,-1)*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_topSFUp' : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_topSFDown' : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_bcUp'   : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsf_bcUp*btagsfZ_bcUp*toptagsf',
                       'SigWts_bcDown'   : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsf_bcDown*btagsfZ_bcDown*toptagsf',
                       'SigWts_lUp'   : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsf_lUp*btagsfZ_lUp*toptagsf',
                       'SigWts_lDown'   : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsf_lDown*btagsfZ_lDown*toptagsf',
                       'SigWts_HTUp'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_HTDown'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       #'Cuts'  : ' ptAK8[idxAK8[0]]>500 && ptAK8[idxAK8[1]]>300 && (idxAK8 == idxAK8[0] || idxAK8 == idxAK8[1]) && ht>1100&&(@idxHTagged.size()==0&&@idxAntiHTagged.size()>0&&@idxTopTagged.size()==0)&&Max$(abs(etaAK4))>1.5',
                       #'Cuts'  : ' ptAK8[idxAK8[0]]>400 && ptAK8[idxAK8[1]]>200 && (idxAK8[0] == idxAntiHTagged || idxAK8[1] == idxAntiHTagged) && ht>1100 && isRegionA && ptAntiHTagged > 300',
                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850&&ptAK8[idxAK8[0]]>400&&PrunedMassAK8[idxAK8[0]]>50&&isRegionA',
#                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&  ptAK8[idxAK8[0]]>500 && PrunedMassAK8[idxAK8[0]]>50 && isRegionA && ptAntiHTagged>500 && ptAntiTopTagged>500',
                       #'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&  ptAK8[idxAK8[0]]>400 && PrunedMassAK8[idxAK8[0]]>50 && @idxAntiTopTagged.size()>0 && @idxAntiHTagged.size()>0 && @idxTopTagged.size()==0 && @idxHTagged.size()==0',
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '25',
                       'xLabel' : 'M_{T} [GeV]',
                       'yLabel' : 'Events/50GeV',
                       'log'   : True
                     }
            }
isRegionB_mt_tZ = {
              'mtprimeBTilde_tM_ZB' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_topSFUp'   : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_topSFDown'   : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_bcUp'   : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsf_bcUp*btagsfZ_bcUp*toptagsf',
                       'Wts_bcDown'   : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsf_bcDown*btagsfZ_bcDown*toptagsf',
                       'Wts_lUp'   : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsf_lUp*btagsfZ_lUp*toptagsf',
                       'Wts_lDown'   : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsf_lDown*btagsfZ_lDown*toptagsf',
                       'Wts_HTUp'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ*QuadWeightHT(ht,1)',
                       'Wts_HTDown'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ*QuadWeightHT(ht,-1)',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_topSFUp'   : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_topSFDown'   : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_bcUp' : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsf_bcUp*btagsfZ_bcUp*toptagsf',
                       'SigWts_bcDown' : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsf_bcDown*btagsfZ_bcDown*toptagsf',
                       'SigWts_lUp' : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsf_lUp*btagsfZ_lUp*toptagsf',
                       'SigWts_lDown' : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsf_lDown*btagsfZ_lDown*toptagsf',
                       'SigWts_HTUp'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_HTDown'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Cuts'  : ' ptAK8[idxAK8[0]]>400 && ptAK8[idxAK8[1]]>300 && (idxAK8[0] == idxAntiHTagged && idxAK8[1] == idxTopTagged) || (idxAK8[1] == idxAntiHTagged && idxAK8[0] == idxTopTagged) && ht>1100&&isRegionB && ptAntiHTagged > 300',
#                       'Cuts'  : ' ptAK8[idxAK8[0]]>400 && ptAK8[idxAK8[1]]>200 && @idxHTagged.size()==0 && @idxAntiHTagged.size()>0 && @idxTopTagged.size()>0 && ptTopTagged>400&&(tau3TopTagged/tau2TopTagged)<0.5&&SoftDropMassTopTagged<220&&SoftDropMassTopTagged>=105&&max(sj0CSVTopTagged,sj1CSVTopTagged)>=0.460 && dR(etaAntiHTagged,phiAntiHTagged,etaTopTagged,phiTopTagged)>2.0',
                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850&&ptAK8[idxAK8[0]]>400&&PrunedMassAK8[idxAK8[0]]>50&&isRegionB',
#                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&  ptAK8[idxAK8[0]]>500 && PrunedMassAK8[idxAK8[0]]>50 && isRegionB && ptAntiHTagged>500 && ptTopTagged>500',
#                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&  ptAK8[idxAK8[0]]>400 && PrunedMassAK8[idxAK8[0]]>50 && @idxAntiHTagged.size()>0 && @idxTopTagged.size()>0 && @idxHTagged.size()==0',
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '25',
                       'xLabel' : 'M_{T} [GeV]',
                       'yLabel' : 'Events/50GeV',
                       'log'   : True
                     }
            }
isRegionC_mt_tZ = {
              'mtprimeCTilde_tM_ZB' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_topSFUp'   : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_topSFDown'   : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_bcUp'   : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsf_bcUp*btagsfZ_bcUp*toptagsf',
                       'Wts_bcDown'   : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsf_bcDown*btagsfZ_bcDown*toptagsf',
                       'Wts_lUp'   : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsf_lUp*btagsfZ_lUp*toptagsf',
                       'Wts_lDown'   : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsf_lDown*btagsfZ_lDown*toptagsf',
                       'Wts_HTUp'   : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,1)*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_HTDown'   : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,-1)*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_topSFUp'   : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_topSFDown'   : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_bcUp'   : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsf_bcUp*btagsfZ_bcUp*toptagsf',
                       'SigWts_bcDown'   : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsf_bcDown*btagsfZ_bcDown*toptagsf',
                       'SigWts_lUp'   : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsf_lUp*btagsfZ_lUp*toptagsf',
                       'SigWts_lDown'   : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsf_lDown*btagsfZ_lDown*toptagsf',
                       'SigWts_HTUp'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_HTDown'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Cuts'  : ' ptAK8[idxAK8[0]]>500 && ptAK8[idxAK8[1]]>300 && (idxAK8 == idxAK8[0] || idxAK8 == idxAK8[1]) && ht>1100&&(@idxHTagged.size()>0&&@idxAntiHTagged.size()>=0&&@idxTopTagged.size()==0)&&isRegionC&&Max$(abs(etaAK4))>1.5',
                       #'Cuts'  : ' ptAK8[idxAK8[0]]>400 && ptAK8[idxAK8[1]]>300 && (idxAK8[0] == idxHTagged || idxAK8[1] == idxHTagged)  && ht>1100&&isRegionC ',
#                       'Cuts'  : ' ptAK8[idxAK8[0]]>400 && ptAK8[idxAK8[1]]>200 && @idxHTagged.size()>0 && @idxAntiHTagged.size()>=0 && @idxTopTagged.size()>0 && ptTopTagged>400&&(tau3TopTagged/tau2TopTagged)<0.5&&SoftDropMassTopTagged<220&&SoftDropMassTopTagged>=105&&max(sj0CSVTopTagged,sj1CSVTopTagged)<0.460 && dR(etaHTagged,phiHTagged,etaTopTagged,phiTopTagged)>2.0',
                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850&&ptAK8[idxAK8[0]]>400&&PrunedMassAK8[idxAK8[0]]>50&&isRegionC',
#                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&  ptAK8[idxAK8[0]]>500 && PrunedMassAK8[idxAK8[0]]>50 && isRegionC && ptHTagged>500 && ptAntiTopTagged>500',
#                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&  ptAK8[idxAK8[0]]>400 && PrunedMassAK8[idxAK8[0]]>50 && @idxHTagged.size()>0 && @idxAntiTopTagged.size()>0 && @idxTopTagged.size()==0',
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '25',
                       'xLabel' : 'M_{T} [GeV]',
                       'yLabel' : 'Events/50GeV',
                       'log'   : True
                     }
            }
isRegionD_mt_tZ = {
              'mtprimeDTilde_tM_ZB' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_HTUp'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ*QuadWeightHT(ht,1)',
                       'Wts_HTDown'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ*QuadWeightHT(ht,-1)',
                       'Wts_bcUp'   : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsf_bcUp*btagsfZ_bcUp*toptagsf',
                       'Wts_bcDown'   : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsf_bcDown*btagsfZ_bcDown*toptagsf',
                       'Wts_lUp'   : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsf_lUp*btagsfZ_lUp*toptagsf',
                       'Wts_lDown'   : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsf_lDown*btagsfZ_lDown*toptagsf',
                       'Wts_topSFUp'   : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_topSFDown'   : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_HTUp'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_HTDown'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_bcUp'   : 'EvtWeight*EvtWtPV*btagsfMed_bcUp*btagsfLoose_bcUp*btagsf_bcUp*btagsfZ_bcUp*toptagsf',
                       'SigWts_bcDown'   : 'EvtWeight*EvtWtPV*btagsfMed_bcDown*btagsfLoose_bcDown*btagsf_bcDown*btagsfZ_bcDown*toptagsf',
                       'SigWts_lUp'   : 'EvtWeight*EvtWtPV*btagsfMed_lUp*btagsfLoose_lUp*btagsf_lUp*btagsfZ_lUp*toptagsf',
                       'SigWts_lDown'   : 'EvtWeight*EvtWtPV*btagsfMed_lDown*btagsfLoose_lDown*btagsf_lDown*btagsfZ_lDown*toptagsf',
                       'SigWts_topSFUp'   : 'EvtWeight*EvtWtPV*toptagsf_Up*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_topSFDown'   : 'EvtWeight*EvtWtPV*toptagsf_Down*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'Wts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrUp'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[5]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
                       'SigWts_mufrDown'   : 'EvtWeight*EvtWtPV*SelectedEvent_lhewts.second[9]*toptagsf*btagsfMed*btagsfLoose*btagsf*btagsfZ',
#                       'Cuts'  : ' ptAK8[idxAK8[0]]>400 && ptAK8[idxAK8[1]]>300 && @idxHTagged.size()>0 && @idxAntiHTagged.size()>=0 && @idxTopTagged.size()>0 && ptTopTagged>400&&(tau3TopTagged/tau2TopTagged)<0.5&&SoftDropMassTopTagged<220&&SoftDropMassTopTagged>=105&&max(sj0CSVTopTagged,sj1CSVTopTagged)>=0.460 && dR(etaHTagged,phiHTagged,etaTopTagged,phiTopTagged)>2.0 ',
                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850&&ptAK8[idxAK8[0]]>400&&PrunedMassAK8[idxAK8[0]]>50&&isRegionD',
#                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&   ptAK8[idxAK8[0]]>500 && PrunedMassAK8[idxAK8[0]]>50 && isRegionD && ptHTagged>500 && ptTopTagged>500',
#                       'Cuts'  : '(ptAK8[0]+ptAK8[1])>850 &&   ptAK8[idxAK8[0]]>400 && PrunedMassAK8[idxAK8[0]]>50 && @idxHTagged.size()>0 && @idxTopTagged.size()>0',
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '25',
                       'xLabel' : 'M_{T} [GeV]',
                       'yLabel' : 'Events/50GeV',
                       'log'   : True
                     }
               }
