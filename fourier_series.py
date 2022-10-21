import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.fft import irfft

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"



def square_wave(t, f, order, Amp):
    Square = Amp / 2
    for i in range(order + 1):
        if i % 2 != 0:
            Square = Square + (2 * Amp / np.pi) * (1 / i) * np.sin(2 * np.pi * f * t * i)
    return Square

#initial data
#square frequency
f = 100
#square order
Order = 5
#Amplitude
A=1

#Data for tran
t_tran  = np.linspace(0.0, 3/f, 500, endpoint=False)
square_tran = square_wave(t = t_tran , f=f, order=Order, Amp=A)
plt.figure()
plt.title(f'Tran. N={Order}')
plt.plot(t_tran, square_tran)
plt.xlabel('t, с')
plt.ylabel('U, В')
plt.grid()
plt.savefig('DATA/mixer_theory/tran_square.jpg')

#Data for spectrum
#N samples
N = 2**14
# sample freq
fs=8*f
#sample period
T = 1.0 / fs

t_spec = np.linspace(0.0, N*T, N, endpoint=False)
double_sideband = fft(square_wave(t = t_spec , f=f, order=Order, Amp=A))
xf = fftfreq(N, T)[:N]

plt.figure()
plt.title(f'Spectrum. N={Order}')
plt.plot(xf, 1/N * np.abs(double_sideband[0:N]))
plt.xlabel('F, Гц')
plt.ylabel('U, В')
plt.grid()
plt.savefig('DATA/mixer_theory/spec_square.jpg')

plt.show()
