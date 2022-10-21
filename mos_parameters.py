import matplotlib.pyplot as plt
import numpy as np

def N(xval, XY):
    flag=0
    counter=0
    for N in XY:
        if N<=xval and flag==0:
            counter = counter + 1
        else:
            flag=1
    return counter

def Vt_v(x1, x2, y1, y2):
    Vt = ((-y1)/(y2-y1))*(x2-x1)+x1
    return Vt

def uCox_v(x1, x2, y1, y2, W, L):
    K= (y2-y1)/(x2-x1)
    uCox =K*L/W
    return uCox

def mos_parameters(X,Y,vX1,vX2,W,L):
    N1 = N(vX1, X)
    N2 = N(vX2, X)
    X1 = X[N1]
    X2 = X[N2]
    Y1 = Y[N1]
    Y2 = Y[N2]
    Vt=Vt_v(X1, X2, Y1, Y2)
    uCox=uCox_v(X1, X2, Y1, Y2, W, L)

    #plot approximation line
    x_line=np.linspace(Vt, 1.2, 100)
    y_line=uCox*(W/L)*(x_line-X1)+Y1

    #output characteristics
    print(f'Threshold voltage {Vt}, В')
    print(f'Koefficient uCox {uCox*1e6}, мкА/(В^2)')

    #plot transconductance
    plt.figure()
    plt.plot(X, Y, linewidth=3, label=f'Vt={round(Vt,2)} В, uCox={round(uCox*1e6,2)} мкА/(В^2)')
    plt.plot(x_line, y_line, linewidth=3, label='approxim')
    plt.xlabel('Vin, В')
    plt.ylabel('gm, См')
    plt.legend()
    plt.grid(which='both', axis='both')


File = 'gm_plots_W=10u_L=550n.csv'
gm = np.genfromtxt(f'DATA/mos_parameters/{File}', delimiter=',', skip_header=1)

mos_parameters(gm[:,0],gm[:,1],0.6,0.9,10e-6,550e-9)


plt.show()