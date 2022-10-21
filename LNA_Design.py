

def CG_CS(N=4, Gain_db=20, Veff=0.15, Lmin=380e-9,
          unCox = 120e-6, Vth = 0.65, Rs=50, W_finger=5e-6):
    #gain magnitude
    Gain=10**(Gain_db/20)

    #transconductance
    gm_CG=1/Rs
    gm_CS=gm_CG*N

    #currents
    I_CG = gm_CG*Veff/2
    I_CS = gm_CS*Veff/2

    #resistances
    R_CG = Gain/gm_CG
    R_CS = Gain/gm_CS

    #dimensions of transistors
    W_CG = (2 * I_CG * Lmin) / (unCox * Veff ** 2)
    W_CS = (2 * I_CS * Lmin) / (unCox * Veff ** 2)

    #number of fingers
    nf_CG = int(W_CG / W_finger)
    nf_CS = nf_CG*N

    print('#------------------------#')
    print(f'CG-CS differential LNA')
    print('#------------------------#')
    print(f'Common gate amplifier')
    print(f'Current CG {I_CG*1e3} mA')
    print(f'R_CG {R_CG} Ohm')
    print(f'Voltage drop on R {R_CG*I_CG} V')
    print(f'Transconductance {gm_CG*1e3} mS')
    print(f'Finger width {W_finger*1e6} um')
    print(f'Number fingers {nf_CG }')
    print(f'Bias Voltage {Vth+Veff} V')

    print('--------------------------')

    print(f'Common source amplifier')
    print(f'Current CS {I_CS*1e3} mA')
    print(f'R_CG {R_CS} Ohm')
    print(f'Voltage drop on R {R_CS * I_CS} V')
    print(f'Transconductance {gm_CS*1e3} mS')
    print(f'Finger width {W_finger*1e6} um')
    print(f'Number fingers {nf_CS }')
    print(f'Bias Voltage {Vth + Veff} V')

    print('--------------------------')

    print(f'Total Id {(I_CG+I_CS)*1e3} mA')

def CS_CS(N=4, Gain_db=20, Veff=0.15, Lmin=380e-9,
          unCox = 120e-6, Vth = 0.65, Rs=50, W_finger=5e-6):

    Gain = 10**(Gain_db/20)

    #transconductance
    gm_CS1 = 1/Rs
    gm_CS2 = gm_CS1 / N

    #currents
    I_CS1 = gm_CS1 * Veff / 2
    I_CS2 = gm_CS2 * Veff / 2

    #resistances
    R_CS1 = Gain/gm_CS1
    R_CS2 = 1/gm_CS2

    #dimensions of transistors
    W_CS1 = (2 * I_CS1 * Lmin) / (unCox * Veff ** 2)
    W_CS2 = (2 * I_CS2 * Lmin) / (unCox * Veff ** 2)

    #number of fingers
    nf_CS1 = int(W_CS1 / W_finger)
    nf_CS2 = nf_CS1/N

    print('#------------------------#')
    print(f'CS-CS differential LNA')
    print('#------------------------#')
    print(f'Common source amplifier 1')
    print(f'Current CS {I_CS1 * 1e3} mA')
    print(f'R_CG {R_CS1} Ohm')
    print(f'Voltage drop on R {R_CS1 * I_CS1} V')
    print(f'Transconductance {gm_CS1 * 1e3} mS')
    print(f'Finger width {W_finger * 1e6} um')
    print(f'Number fingers {nf_CS1}')
    print(f'Bias Voltage {Vth + Veff} V')

    print('--------------------------')

    print(f'Common source amplifier 2')
    print(f'Current CS {I_CS2 * 1e3} mA')
    print(f'R_CG {R_CS2} Ohm')
    print(f'Voltage drop on R {R_CS2 * I_CS2} V')
    print(f'Transconductance {gm_CS2 * 1e3} mS')
    print(f'Finger width {W_finger * 1e6} um')
    print(f'Number fingers {nf_CS2}')
    print(f'Bias Voltage {Vth + Veff} V')

    print('--------------------------')

    print(f'Total Id {(I_CS1 + I_CS2) * 1e3} mA')

CG_CS(N=4, Gain_db=20, Veff=0.15, Lmin=380e-9,
      unCox = 120e-6, Vth = 0.65, Rs=50, W_finger=10e-6)

CS_CS(N=4, Gain_db=20, Veff=0.3, Lmin=380e-9,
          unCox = 120e-6, Vth = 0.65, Rs=50, W_finger=7e-6)

