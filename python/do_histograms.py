from   anaTp  import *
from variableDictionaries_cfi import *

sample = 'Nominal'
Wts = 'Wts'
SigWts = 'SigWts'
output = True 
jetType = 'CHS'
outFileName = 'presel_QCDPt_Z_27Aug17.root'
QCDType = 'Pt'
analysis(preselDict, sample, Wts, SigWts, output, outFileName, jetType, QCDType)
outFileName = 'presel_QCDHT_Wt_Z_27Aug17.root'
QCDType = 'HT'
analysis(preselDict_Wt, sample, Wts, SigWts, output, outFileName, jetType, QCDType)
