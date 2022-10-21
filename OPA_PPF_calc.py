#Constants for Transistors
import numpy as np

K=7.037e-25
hamma = 0.691

T=300
k=1.38e-23

upCox=55e-6
unCox=150e-6
Cox=4.29e-3

L_test=550e-9

lambda_p=40e-3
lambda_n=80e-3


def gm_W(Id, Veff, L, Type="N"):
    gm = 2 * Id / Veff
    if Type=="N":
        W = gm * L / (unCox * Veff)
        r_out = (L/L_test)/(lambda_n*Id)
    else:
        W = gm * L / (upCox * Veff)
        r_out = (L / L_test) / (lambda_p * Id)
    return gm, W, r_out

def flicker_thermal(Id, Veff,L, Type="N"):
    gm, W, _ = gm_W(Id, Veff,L, Type)
    flicker_f = K/(W*L*Cox)*gm/(4*k*T*hamma)
    if Type == "N":
        thermal_v = ((4 * k * T * hamma * L) / (unCox * W * Veff))**0.5
    else:
        thermal_v = ((4 * k * T * hamma * L) / (upCox * W * Veff))**0.5
    return flicker_f, thermal_v

def print_par(Title,gm, W, L, rout, fc, thermal_v):
    print(f'{Title}')
    print(f'Transconductance: {gm*1e6} uS')
    print(f'Width: {W * 1e6} um')
    print(f'Length: {L * 1e6} um')
    print(f'Output resistance: {rout/1e6} MOhm')
    print(f'1/f corner frequency : {fc/1e3} kHz')
    print(f'Thermal noise voltage : {thermal_v*1e9} nV/sqrt(Hz)')

#input transistors
L_in = 1e-6
Id=90e-6
Veff1=0.25

gm_in, W_in, r_out_in = gm_W(Id=Id, Veff=Veff1,L=L_in, Type="N")
fc_in, thermal_in = flicker_thermal(Id=Id, Veff=Veff1,L=L_in, Type="N")
print_par(Title='#Input transistor#',gm=gm_in, W=W_in, L=L_in, rout=r_out_in, fc=fc_in, thermal_v=thermal_in)

#load transistors
L_load = 1e-6
gm_load, W_load, r_out_load = gm_W(Id=Id, Veff=Veff1,L=L_load, Type="P")
fc_load, thermal_load = flicker_thermal(Id=Id, Veff=Veff1,L=L_load, Type="P")
print_par(Title='#Load transistor#',gm=gm_load, W=W_load, L=L_load, rout=r_out_load, fc=fc_load, thermal_v=thermal_load)

#tail transistor
L_tail = 1e-6
gm_tail, W_tail, r_out_tail = gm_W(Id=Id*2, Veff=Veff1,L=L_tail, Type="N")
fc_tail, thermal_tail = flicker_thermal(Id=Id*2, Veff=Veff1,L=L_tail, Type="N")
print_par(Title='#Tail transistor#',gm=gm_tail, W=W_tail, L=L_tail, rout=r_out_tail, fc=fc_tail, thermal_v=thermal_tail)

print('#Summarize#')
Total_thermal_noise = thermal_in+thermal_load+thermal_tail
Gain_DM = 20*np.log10(gm_in*r_out_load)
print(f'Input reffered thermal noise: {Total_thermal_noise*1e9}, nV/sqrt(Hz)')
print(f'Gain: {Gain_DM}, dB')



