import matplotlib.pyplot as plt
import numpy as np
from Functions import read_file

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"



#---Inition Conditions---
R = 25e3
C = 12e-12
Overlap_C = 50
N_Bit = 4
Unity_Cap = C*(1+Overlap_C/100)/2**N_Bit
#------------------------

print(f'Разрядность системы: {N_Bit}')
print(f'Минимальная  емкость: {Unity_Cap} Ф')
print(f'Максимальная емкость: {Unity_Cap*(2**N_Bit-1)} Ф')

##-----------
N_Points = 1000
Number_Val = 2**N_Bit-1
pi = 3.1415
Bank_Cap =  np.zeros([Number_Val], float)
##-----------

#Calculate discrete capacitances
for i in range(Number_Val):
    Bank_Cap[i]=Unity_Cap*(Number_Val-i)


#Create massives
Val_CAP=np.linspace(np.max(Bank_Cap), np.min(Bank_Cap), N_Points)
F_CAP = np.zeros([len(Val_CAP)], float)
F_CAP = 1/(2*pi*Val_CAP*R)
Frequency_ideal = np.zeros([len(Val_CAP)], float)
Frequency_real =  np.zeros([len(Val_CAP)], float)

#Calculate ideal frequencies
Frequency_ideal = 1/(2*pi*R*Val_CAP)

#Calculate real frequencies
k=0
for i in range(len(Val_CAP)):
    if Val_CAP[i]>=Bank_Cap[k]:
        Frequency_real[i]= 1/(2*pi*R*Bank_Cap[k])
    else:
        k += 1
        Frequency_real[i] = 1 / (2*pi*R*Bank_Cap[k])


#Plot Figures

plt.figure()
plt.plot(F_CAP, Frequency_real, linewidth='3', label='Calculated')
#plt.plot(Simulation_F[:, 0], Simulation_F[:, 1], linewidth='3', label='Simulated')
plt.plot(F_CAP, Frequency_ideal, linewidth='3',label='Ideal' )
plt.xlim([np.min(F_CAP), np.max(F_CAP)/6])
plt.ylim([np.min(F_CAP), np.max(F_CAP)/6])
plt.ylabel('OUT F, Гц')
plt.xlabel('IN F,Гц')
plt.legend()
plt.grid()

plt.figure()
plt.plot(F_CAP, Frequency_real-Frequency_ideal, linewidth='3',label='Calculated' )
#plt.plot(Simulation_F[:, 0], Simulation_F[:, 2], linewidth=3, label='Simulated')
plt.xlim([np.min(F_CAP), np.max(F_CAP)/6])
plt.ylim([0, 1e6])
plt.grid()
plt.legend()
plt.ylabel('Error F, Гц')
plt.xlabel('IN F,Гц')

plt.figure()
plt.plot(Val_CAP, Frequency_real, linewidth='3', label='Calculated')
plt.plot(Val_CAP, Frequency_ideal, linewidth='3',label='Ideal', c='Tab:green' )
plt.xlim([np.max(Val_CAP), np.min(Val_CAP)])
plt.ylabel('OUT F, Гц')
plt.xlabel('C,Ф')
plt.legend()
plt.grid()

plt.show()