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

Vt=0.55

Veff1=0.2
Veff2=0.2
VDD=3.3
Id=500e-6
Av=10
Vp_LO=0.3


Vr_max = VDD-(Veff1+(1+(2**0.5)/2)*Veff2)
Rmax = 2*Vr_max/Id

gm=2*Id/Veff1
R = Av*np.pi/(2*gm)
Vn_in = (4*k*T*(hamma/gm+1/(gm**2*R)))**0.5

W_in = 2*Id*L_test/(unCox*Veff1**2)
W_sw = 2*(Id/2)*L_test/(unCox*Veff2**2)


print(f'Rmax = {Rmax/1000} кОм')
print(f'gm = {gm*1e3} мСм')
print(f'R = {R/1000} кОм')
print(f'Gain = {20*np.log10(2/np.pi*gm*R)} дБ')
print(f'Input noise {Vn_in*1e9} nV/sqrt(Hz)')
print(f'NF = {10*np.log10(1+Vn_in**2/(4*k*T*50))} дБ')

print(f'W_in {W_in*1e6} мкм')
print(f'W_sw {W_sw*1e6} мкм')
print(f'L = {L_test*1e6} мкм')
print(f'Id = {Id*1e3} мА')
print(f'Vgs_1 = {Veff1+Vt} В')


#reduce gain coefficient

Vp_reduce = 1-2*Veff2/(5*np.pi*Vp_LO)
print(20*np.log10(Vp_reduce))

