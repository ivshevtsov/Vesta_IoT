import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

Home='DATA/Test_RX/data'

#Gains
HF_max = np.genfromtxt(f'{Home}/IoT_max_Gain.vcsv', delimiter=',', skip_header=6)
HF_min = np.genfromtxt(f'{Home}/IoT_min_Gain.vcsv', delimiter=',', skip_header=6)

#Compression gains
P1db_max = np.genfromtxt(f'{Home}/IoT_P1db_max_gain.csv', delimiter=',', skip_header=1)
P1db_min = np.genfromtxt(f'{Home}/IoT_P1db_min_gain.csv', delimiter=',', skip_header=1)

#NF
NF_ssb = np.genfromtxt(f'{Home}/IoT_nf_dsb_max_gain.vcsv', delimiter=',', skip_header=6)

#Tran
DCOC_ON=np.genfromtxt(f'{Home}/Tran_max_gain_DCOC_on.vcsv', delimiter=',', skip_header=6)
DCOC_OFF=np.genfromtxt(f'{Home}/Tran_max_gain_DCOC_off.vcsv', delimiter=',', skip_header=6)

plt.figure()
plt.title('RX NB-IoT(Tran)')
plt.plot(DCOC_ON[:,0], DCOC_ON[:,1], linewidth=3, label='DCOC ON')
plt.plot(DCOC_OFF[:,0], DCOC_OFF[:,1], linewidth=3, label='DCOC OFF')
plt.legend()
plt.xlabel('t, с')
plt.ylabel('U, В')
plt.grid(which='both', axis='both')



'''
plt.figure()
plt.title('RX NB-IoT(NF DSB)')
plt.semilogx(NF_ssb[:,0], NF_ssb[:,1]-3, linewidth=3)
plt.xlabel('F, Гц')
plt.ylabel('NF(DSB), дБ')
plt.grid(which='both', axis='both')



plt.figure()
plt.title('RX NB-IoT')
plt.semilogx(HF_max[:,0], HF_max[:,1], linewidth=3)
plt.semilogx(HF_min[:,0], HF_min[:,1], linewidth=3)
plt.xlabel('F, Гц')
plt.ylabel('H(f), дБ')
plt.grid(which='both', axis='both')


plt.figure()
plt.title('RX NB-IoT(max)')
plt.plot(P1db_max[:,0], P1db_max[:,1], linewidth=3)
plt.xlabel('Pin, дБм')
plt.ylabel('Pout, дБм')
plt.grid(which='both', axis='both')

plt.figure()
plt.title('RX NB-IoT(min)')
plt.plot(P1db_min[:,0], P1db_min[:,1], linewidth=3)
plt.xlabel('Pin, дБм')
plt.ylabel('Pout, дБм')
plt.grid(which='both', axis='both')
'''






plt.show()


