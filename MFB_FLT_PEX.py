import openpyxl
from numpy import genfromtxt
import numpy as np

HOME = 'DATA/MFB_Filter/csv'
File = 'mfb_mism_pex'



#PEX results
PEX_DATA = genfromtxt(f'{HOME}/{File}.csv', delimiter=',', skip_header=True)

Gain = 13
BW =14
Att = 15
d_GD = 17
NF = 18
Id = 20
offset_dc = 21
LIST_PAR=[BW, Gain, Att, d_GD, NF, offset_dc, Id]


for N in LIST_PAR:
    LIST = []
    for i in range(len(PEX_DATA)):
        LIST.append(PEX_DATA[i][N])
    print(f'{N}  -  {np.std(LIST)}')
