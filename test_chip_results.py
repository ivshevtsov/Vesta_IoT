import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import windows

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

HOME = 'DATA\Test_chip'
File_THRU = 'TEST_THRU.csv'

list_files = ['TEST_LPF_MODEM_I.csv',
              'TEST_LPF_MODEM_Q.csv',
              'TEST_LPF_GNSS_I.csv',
              'TEST_LPF_GNSS_Q.csv',
              'TEST_VGA_MODEM.csv',
              'TEST_VGA_GNSS.csv',
              'TEST_MIX_MODEM.csv',
              'TEST_ENV_m06.csv',
              'TEST_THRU.csv',
              'TEST_MFB_MODEM.csv',
              'TEST_VGA_GNSS_SE.csv']



BIT = 7
Data_THRU = np.genfromtxt(f'{HOME}/csv/{list_files[8]}', delimiter=',', skip_header=1)
Data_MEAS = np.genfromtxt(f'{HOME}/csv/{list_files[BIT]}', delimiter=',', skip_header=1)




#Plot
plt.figure()
#plt.plot(Data_THRU[:,0], Data_THRU[:,1],label='THRU', linewidth=2)
#plt.plot(Data_MEAS[:,0], Data_MEAS[:,1],label='RAW DATA', linewidth=2)
#plt.plot(Data_MEAS[:,0], Data_MEAS[:,1]-Data_THRU[:,1],label=list_files[BIT][:-4], linewidth=2)
#plt.plot(Data_MEAS[:, 0], Data_MEAS[:, 3], label='ENV IN', linewidth=2)
#plt.plot(Data_MEAS[:, 0], Data_MEAS[:, 1], label='ENV OUT', linewidth=2)

#plt.xscale('log')
plt.xlabel('t, c')
plt.ylabel('V')
plt.legend()
plt.grid(which='both', axis='both')



Data = Data_MEAS[:, 3]

#initial data
dT = 1e-9
SAMPLE_RATE = 1/dT
N = len(Data)
##------------------
##Calculate spectrum
yf = fft(Data)
xf = fftfreq(N, 1/SAMPLE_RATE)

w = windows.blackman(N)
ywf = fft(Data*w)
##------------------

#freq = 10e7
#divide = int(10e7/freq)
#print(max(xf[0:N//2]))

plt.figure()

plt.plot(xf[0:N//(2)], 20*np.log10(yf[0:N//(2)]*(2/N)), label='Rectangular')
#plt.plot(xf[0:N//(2)], 20*np.log10(ywf[0:N//(2)]*(2/N)), label='Blackman')
plt.legend()
plt.xlabel('f, Гц')
plt.ylabel('дБ')
plt.subplots_adjust(left=0.06, bottom=0.135, right=0.97, top=0.92, wspace=None, hspace=None)
plt.grid()



plt.show()












