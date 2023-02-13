import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

def Cascaded_gain(Gain):
    result=[]
    x=[]
    Gain_sum=0
    for i in range(len(Gain)):
        Gain_sum = Gain_sum +Gain[i]
        result.append(Gain_sum)
        x.append(i+1)
    return x, result

def Cascaded_noise(Noise, Gain):
    result=[]
    x=[1]
    result.append(Noise[0])
    Gain_Cascaded = 1
    NF_Cascaded = 10 ** (Noise[0] / 10)
    for i in range(len(Noise) - 1):
        Gain_Cascaded = Gain_Cascaded * (10 ** (Gain[i] / 10))
        NF_block = 10 ** (Noise[i + 1] / 10)
        NF_Cascaded = NF_Cascaded + (NF_block - 1) / Gain_Cascaded
        result.append(10*np.log10(NF_Cascaded))
        x.append(i+2)
    return x, result

def Cascaded_P1dB(Gain, P1db):
    result = []
    x=[1]
    result.append(P1db[0])
    P1db_sum = 1/(10**(P1db[0]/10))
    Cascaded_gain=1
    for i in range(len(P1db)-1):
        Cascaded_gain=Cascaded_gain*(10**(Gain[i]/10))
        P1db_sum = P1db_sum +  Cascaded_gain/(10**(P1db[i+1]/10))
        result.append(10*np.log10(1/P1db_sum))
        x.append(i+2)
    return x, result

def Plot_with_dots(x, y, Legend, XLabel, YLabel, N_Fig):
    plt.figure(N_Fig)
    plt.plot(x, y, linewidth='3')
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'o', label=f'{i + 1}.{Legend[i]}')
    plt.ylabel(YLabel)
    plt.xlabel(XLabel)
    plt.legend()
    plt.grid()

HOME='DATA/Budget'
#ADC characteristics
ADC_FS = 4

#Input signal characteristics
Pmax = -28
Pmin = -108.2


#input signals
print('Input Signals')
print(f'Min input signal {Pmin} дБм')
print(f'Max input signal {Pmax} дБм')
print()

#min/max gain receiver chain
print('Gain')
print(f'min gain = {ADC_FS-Pmax} дБ')
print(f'max gain = {ADC_FS-Pmin} дБ')
print()

#compression point/IIP3 RF chain
print('Linearity')
P1db=Pmax+3
print(f'P1dB_in = {P1db} дБм')
print(f'IIP3_in = {P1db+10} дБм')

#Sensetivity



#Blocks characteristics
mode='min'

if mode =='max':
    # Input power
    IN_Power = Pmin
    #LNA
    LNA_G=20.79
    LNA_NF = 3.61
    LNA_P1dB = -5.07
    LNA_Band = 300e6

    #Mixer
    MIX_G=19.38
    MIX_NF = 19
    MIX_P1dB = -10
    MIX_Band = 300e6

    #Filter
    LPF_G=15
    LPF_NF = 36
    LPF_P1dB = -10
    LPF_Band = 200e3

    #VGA Gain calculation

    VGA_G=(ADC_FS-(IN_Power))-LNA_G-MIX_G-LPF_G
    VGA_NF = 45
    VGA_P1dB = -20
    VGA_Band = 200e3
    print(f'VGA_GAIN={VGA_G}')
else:
    # Input power
    IN_Power = Pmax
    # LNA
    LNA_G = 10.87
    LNA_NF = 7.86
    LNA_P1dB = -5
    LNA_Band = 800e6
    # Mixer
    MIX_G = 10
    MIX_NF = 30
    MIX_P1dB = -0.6
    MIX_Band = 300e6

    # Filter
    LPF_G = 2
    LPF_NF = 46
    LPF_P1dB = 10
    LPF_Band = 200e3

    # VGA Gain calculation

    VGA_G = (ADC_FS - (IN_Power)) - LNA_G - MIX_G - LPF_G
    VGA_NF = 45
    VGA_P1dB = 3
    VGA_Band = 200e3
    print(f'VGA_GAIN={VGA_G}')

##----Receiver Gain-----##
Gain_dB = [LNA_G, MIX_G, LPF_G, VGA_G]
##----Receiver Noise-----##
NF_dB = [LNA_NF, MIX_NF, LPF_NF, VGA_NF]
##----Receiver P1dB-----##
P1dB_dBm = [LNA_P1dB, MIX_P1dB, LPF_P1dB, VGA_P1dB]
##----Receiver Bands-----##
Band_GPS_BLOCKS = [LNA_Band, MIX_Band, LPF_Band, VGA_Band]


##----Receiver Legend-----##
Legend = ['МШУ', 'Смеситель', 'LPF', 'VGA']


#Cascaded NF
x_1, y_1 = Cascaded_noise(NF_dB, Gain_dB)
Plot_with_dots(x_1, y_1, Legend=Legend, XLabel='N', YLabel='NF, дБ', N_Fig=1)
plt.savefig(f'{HOME}/NF_{mode}.png')

#Cascaded Gain
x_2, y_2=Cascaded_gain(Gain_dB)
Plot_with_dots(x_2, y_2, Legend=Legend, XLabel='N', YLabel='Gain, дБ', N_Fig=2)
plt.savefig(f'{HOME}/Gain_{mode}.png')

#Cascaded P1dB
x_3, y_3 = Cascaded_P1dB(Gain_dB, P1dB_dBm)
Plot_with_dots(x_3, y_3, Legend=Legend, XLabel='N', YLabel='P1dB(IN), дБм', N_Fig=3)
plt.savefig(f'{HOME}/P1dB_{mode}.png')

plt.show()