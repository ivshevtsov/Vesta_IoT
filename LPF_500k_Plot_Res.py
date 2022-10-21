import matplotlib.pyplot as plt
import numpy as np

File = 'LPF_HF_500k.csv'
HF = np.genfromtxt(f'DATA/lpf_500k/{File}', delimiter=',', skip_header=1)


#Plot H(f)
plt.figure()
plt.title(f'Butterworth. N=3')
plt.semilogx(HF[:,0], HF[:,1], linewidth=3)
plt.xlabel('F, Гц')
plt.ylabel('H(f), дБ')
plt.grid(which='both', axis='both')
plt.show()