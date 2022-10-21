import matplotlib.pyplot as plt
import numpy as np
import math

def exp_res(step=1.6):
    R=[]
    R_IN=5000
    R.append( R_IN*(10 ** (0*step / 20)))
    R.append( R_IN*(10 ** (1*step / 20)) - R[0])
    R.append( R_IN*(10 ** (2*step / 20)) - R[0])
    R.append( R_IN*(10 ** (3*step / 20)) - R[0] - R[2])
    R.append( R_IN*(10 ** (4*step / 20)) - R[0])
    R.append( R_IN*(10 ** (5*step / 20)) - R[0] - R[4])
    R.append( R_IN*(10 ** (6*step / 20)) - R[0] - R[4])
    R.append( R_IN*(10 ** (7*step / 20)) - R[0] - R[4] - R[6])
    R.append( R_IN*(10 ** (8*step / 20)))
    R.append( R_IN*(10 ** (9*step / 20)) - R[8])
    R.append( R_IN*(10 ** (10*step / 20)) - R[8])
    R.append(R_IN* (10 ** (11*step / 20)) - R[8] - R[10])
    R.append( R_IN*(10 ** (12*step / 20)) - R[8])
    R.append( R_IN*(10 ** (13*step / 20)) - R[8] - R[12])
    R.append( R_IN*(10 ** (14*step / 20)) - R[8] - R[12])
    R.append( R_IN*(10 ** (15*step / 20)) - R[8] - R[12] - R[14])
    return R

def exponential_func(x1=1, y1=0.18, x2=2, y2=0.2):
    k0 = (1/(x1-x2))*np.log(y1/y2)
    A0 = y1/np.exp(k0*x1)
    print(f'A0={A0}, k0={k0}')
    return A0,k0




R=exp_res(step=1.6)
print(20*np.log10(R[8]+R[12]+R[14]+R[15]))

print('list')
print(*R, sep="\n")
print(R)


R_odd=[R[1], R[3], R[5], R[7], R[9], R[11], R[13], R[15]]
n = [1, 2, 3, 4, 5, 6, 7, 8]
A0,k0=exponential_func(x1=0, y1=R[0], x2=8, y2=R[8])
print(A0*np.exp(k0*12))


plt.figure()
plt.plot(n, R_odd)

Gain=10
Rin=1
Rmax=Rin*Gain
N=5

Rf=np.linspace(1, Rmax, 2**N)
step_db=[]
Gain_db=20*np.log10(Rf/Rin)
for i in range(len(Gain_db)-1):
    step_db.append(Gain_db[i+1]-Gain_db[i])


plt.figure()
plt.plot(Rf, Gain_db)
plt.figure()
plt.plot(Rf[:-1],step_db)
plt.grid()


plt.show()

