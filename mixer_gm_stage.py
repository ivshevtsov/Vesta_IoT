
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


def gm_to_Id(gm, Veff):
    Id = Veff*gm/2
    return Id

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

def print_par(Title,gm,Id, W, L, rout, fc, thermal_v):
    print(f'{Title}')
    print(f'Transconductance: {gm*1e6} uS')
    print(f'Current: {Id * 1e6} uА')
    print(f'Width: {W * 1e6} um')
    print(f'Length: {L * 1e6} um')
    print(f'Output resistance: {rout/1e6} MOhm')
    print(f'1/f corner frequency : {fc/1e3} kHz')
    print(f'Thermal noise voltage : {thermal_v*1e9} nV/sqrt(Hz)')
    print(f'Noise figure {10*np.log10(1+(thermal_v**2)/(4*k*T*50))} дБ')

#typical characteristics
L_in = 550e-9
Veff=0.23
gm=250e-6
#nmos transistor_low_gain
Id = gm_to_Id(gm, Veff)
gm_in, W_in, r_out_in = gm_W(Id=Id, Veff=Veff,L=L_in, Type="N")
fc_in, thermal_in = flicker_thermal(Id=Id, Veff=Veff,L=L_in, Type="N")
print_par(Title='#Input transistor#',gm=gm_in, Id=Id, W=W_in, L=L_in, rout=r_out_in, fc=fc_in, thermal_v=thermal_in)

#pmos transistor_low_gain
Id = gm_to_Id(gm, Veff)
gm_in, W_in, r_out_in = gm_W(Id=Id, Veff=Veff,L=L_in, Type="P")
fc_in, thermal_in = flicker_thermal(Id=Id, Veff=Veff,L=L_in, Type="P")
print_par(Title='#Input transistor#',gm=gm_in, Id=Id, W=W_in, L=L_in, rout=r_out_in, fc=fc_in, thermal_v=thermal_in)

print(f'Total NF  {10*np.log10(1+(2*thermal_in**2)/(4*k*T*50))}')