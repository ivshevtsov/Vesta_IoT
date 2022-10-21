from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams["figure.figsize"] = (12,5)

#define nonlinear system
def nonlinear(x, N):
    result=0
    for i in range(N):
        result = result +x**(i+1)
    return result

#mixer output
def mix_out(input, N):
    return nonlinear(input, N)

def mix_sum(x,y, N):
    return mix_out(x, N)+mix_out(y,N)

def square_wave(t, f, order, Amp):
    Square = Amp / 2
    for i in range(order + 1):
        if i % 2 != 0:
            Square = Square + (2 * Amp / np.pi) * (1 / i) * np.sin(2 * np.pi * f * t * i)
    return Square


# Number of sample points
N = 2**20
# sample spacing
T = 1.0 / 80
x = np.linspace(0.0, N*T, N, endpoint=False)

#input signals
RF = np.cos(10*2.0*np.pi*x)
LO = np.cos(11*2.0*np.pi*x)

#nonlinearity order
Order=3

Single = fft(mix_out(RF+LO, Order))
Single_balanced = fft(mix_out(RF+LO,Order)-mix_out(RF-LO,Order))
Double_balanced = fft(mix_sum(RF+LO, -RF-LO, Order)-mix_sum(-RF+LO, RF-LO,Order))

xf = fftfreq(N, T)[:N//2]

#plt.figure('Single')
plt.subplot(3, 1, 1)
plt.title('Single')
plt.plot(xf, 2/N * np.abs(Single[0:N//2]))
plt.grid()
#plt.figure('Single_balanced')
plt.subplot(3, 1, 2)
plt.title('Single Balanced')
plt.plot(xf, 2/N * np.abs(Single_balanced[0:N//2]))
plt.grid()
#plt.figure('Double_balanced')
plt.subplot(3, 1, 3)
plt.title('Double Balanced')
plt.plot(xf, 2/N * np.abs(Double_balanced[0:N//2]))
plt.grid()
plt.subplots_adjust(left=0.06, bottom=0.1, right=0.97, top=0.92, wspace=None, hspace=0.7)
plt.show()