from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams['lines.linewidth'] = 3
#plt.rcParams["figure.figsize"]=[4,3]


Band = 500e3*np.pi*2
Band_attenuation = 3

Band_stop = 2000e3*np.pi*2
Band_stop_attenuation = 30

N, Wn = signal.buttord(wp=Band, ws=Band_stop, gpass=Band_attenuation, gstop=Band_stop_attenuation, analog=True)
print(f'Filter Bandwidth {Wn/(2*np.pi)} Hz')
print(f'Filter Order {N}')

Orders = [N]
for Order in Orders:
    sc=2*np.pi
    b, a = signal.butter(N=Order, Wn=Wn, analog=True)
    w, h = signal.freqs(b, a, np.logspace(5, 7.5, 500))
    plt.semilogx(w/sc, 20 * np.log10(abs(h)), label = f'Butterworth')

    b, a = signal.cheby1(N=Order, rp=3, Wn=Wn, btype='low', analog=True)
    w, h = signal.freqs(b, a, np.logspace(5, 7.5, 500) )
    plt.semilogx(w/sc, 20 * np.log10(abs(h)), label = f'Chebyshev_1')

plt.title(f'Filter Order={Orders[0]}, Band={round(Wn/(sc*1000),2)} кГц')
plt.legend()
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')
plt.grid(which='both', axis='both')
plt.fill([Band_stop/sc, Band_stop/sc, 3e7/sc, 3e7/sc], [0, -Band_stop_attenuation, -Band_stop_attenuation, 0], '0.9', lw=0) # stop
plt.fill([1e5/sc, 1e5/sc,  Band/sc, Band/sc], [-60, -3, -3, -60], '0.9', lw=0) # pass
plt.show()