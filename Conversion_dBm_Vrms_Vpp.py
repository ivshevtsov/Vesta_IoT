import numpy as np


#https://www.ahsystems.com/EMC-formulas-equations/dBm_Volts_Watts_Conversion.php

def conversion(dBm=None, Vrms=None, Vpp=None, Vp=None, W=None):
    Z = 50
    if dBm!=None:
        Vrms = (Z / 1000) ** 0.5 * 10 ** (dBm / 20)
        Vp = Vrms * (2 ** 0.5)
        Vpp = Vp * 2
        W = 10 ** ((dBm - 30) / 10)
        return dBm, Vrms, Vp, Vpp, W
    elif Vrms!=None:
        dBm = 10*np.log10((Vrms**2*1000)/Z)
        Vp = Vrms * (2 ** 0.5)
        Vpp = Vp * 2
        W = 10 ** ((dBm - 30) / 10)
        return dBm, Vrms, Vp, Vpp, W
    elif Vpp!=None:
        Vp = Vpp/2
        Vrms = Vp/(2**0.5)
        dBm = 10*np.log10((Vrms**2*1000)/Z)
        W = 10 ** ((dBm - 30) / 10)
        return dBm, Vrms, Vp, Vpp, W
    elif Vp!=None:
        Vpp = Vp*2
        Vrms = Vp/(2**0.5)
        dBm = 10*np.log10((Vrms**2*1000)/Z)
        W = 10 ** ((dBm - 30) / 10)
        return dBm, Vrms, Vp, Vpp, W
    elif W!=None:
        dBm = 10 * np.log10(W)+30
        Vrms = (Z / 1000) ** 0.5 * 10 ** (dBm / 20)
        Vp = Vrms * (2 ** 0.5)
        Vpp = Vp * 2
        return dBm, Vrms, Vp, Vpp, W

A=conversion(Vpp=0.117)


print(A)