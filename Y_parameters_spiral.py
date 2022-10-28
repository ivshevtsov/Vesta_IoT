import matplotlib.pyplot as plt
from Functions import read_file
import numpy as np
import skrf as rf
plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


def Fitting_error(File_Model, File_EM_sim):
    S_Model = rf.Network(File_Model)
    S_EM_sim = rf.Network(File_EM_sim)

    n = len(S_Model.f)

    for j in range(2):
        for k in range(2):
            #Calculation denominator(local sum)
            sum_local_im = 0
            sum_local_re = 0
            for i in range(n):
                sum_local_im = sum_local_im + S_EM_sim.y_im[i, j, k] ** 2
                sum_local_re = sum_local_re + S_EM_sim.y_re[i, j, k] ** 2
            sum_local_im = sum_local_im / n
            sum_local_re = sum_local_re / n
            # Calculation numerator(global sum)
            sum_global_im = 0
            sum_global_re = 0
            for i in range(n):
                numerator_im = ((S_EM_sim.y_im[i, j, k] - S_Model.y_im[i, j, k]) ** 2) / sum_local_im
                numerator_re = ((S_EM_sim.y_re[i, j, k] - S_Model.y_re[i, j, k]) ** 2) / sum_local_re
                sum_global_im = sum_global_im + numerator_im
                sum_global_re = sum_global_re + numerator_re
            Error_im = ((sum_global_im / n) ** (1 / 2)) * 100
            Error_re = ((sum_global_re / n) ** (1 / 2)) * 100
            print(f'Error Real(Y{j + 1}{k + 1})(%) = {Error_re}')
            print(f'Error Imag(Y{j + 1}{k + 1})(%) = {Error_im}')


    File_Model = f'Files/Y_Spiral/IND1_TSMC.s2p'
    File_EM_sim =   f'Files/Y_Spiral/IND1_EM_SU.s2p'





#Fitting_error(File_Model = File_Model, File_EM_sim = File_EM_sim)

    Model = rf.Network(File_Model)
    EM_sim =rf.Network(File_EM_sim)


    plt.figure()
    Model.plot_s_db(m=2-1, n=1-1, label=f'TSMC Model', linewidth='3')
    EM_sim.plot_s_db(m=2-1, n=1-1, label=f'EM Simulation', linewidth='3')
    plt.grid()
    plt.ylabel('S11, дБ')
    plt.xlabel('F, Гц')

    plt.figure()
    Model.plot_s_smith(m=0, n=0, label='TSMC model', linewidth='3')
    EM_sim.plot_s_smith(m=0, n=0, label='EM Simulation', linewidth='3')
    plt.grid()


    plt.figure()
    plt.plot(Model.f, Model.z_im[:, 0, 0], label='TSMC model', linewidth='3')
    plt.plot(EM_sim.f, EM_sim.z_im[:, 0, 0], label='EM Simulation', linewidth='3')
    plt.grid()
    plt.legend()
    plt.xlabel('F, Гц')
    plt.ylabel('Z11(Im), Ом')

    plt.figure()
    plt.plot(Model.f, Model.z_re[:, 0, 0], label='TSMC model', linewidth='3')
    plt.plot(EM_sim.f, EM_sim.z_re[:, 0, 0], label='EM Simulation', linewidth='3')
    plt.grid()
    plt.legend()
    plt.xlabel('F, Гц')
    plt.ylabel('Z11(Re), Ом')

HOME = 'DATA/Y_inductor'

File_EM1 = f'{HOME}/EM1_sim.s1p'
File_EM2 = f'{HOME}/EM2_sim.s1p'
File_TSMC = f'{HOME}/TSMC_sim.s1p'
EM1_sim = rf.Network(File_EM1)
EM2_sim = rf.Network(File_EM2)
TSMC_sim = rf.Network(File_TSMC)
#TSMC_sim.se2gmm(1)


#new_freq = rf.Frequency(0.05, 5, 800, 'ghz')
#One_Ind.interpolate_self(new_freq, kind='zero')
#Two_Ind.interpolate_self(new_freq, kind='zero')

plt.figure()
EM1_sim.plot_s_db(m=1-1, n=1-1, label=f'S11(One)', linewidth='3')
EM2_sim.plot_s_db(m=1-1, n=1-1, label=f'S11(Two)', linewidth='3')
TSMC_sim.plot_s_db(m=1-1, n=1-1, label=f'S11(TSMC)', linewidth='3')
plt.grid()
plt.ylabel('SP, дБ')
plt.xlabel('F, Гц')

plt.figure()
plt.plot(EM1_sim.f, EM1_sim.z_im[:, 1-1, 1-1]/EM1_sim.z_re[:, 1-1, 1-1], label='Q(One)', linewidth='3')
plt.plot(EM2_sim.f, EM2_sim.z_im[:, 1-1, 1-1]/EM2_sim.z_re[:, 1-1, 1-1], label='Q(Two)', linewidth='3')
plt.plot(TSMC_sim.f, TSMC_sim.z_im[:, 1-1, 1-1]/TSMC_sim.z_re[:, 1-1, 1-1], label='Q(TSMC)', linewidth='3')
plt.grid()
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('Q')

plt.figure()
plt.plot(EM1_sim.f, EM1_sim.z_im[:, 1-1, 1-1]/(EM1_sim.f*2*np.pi), label='Ind(One)', linewidth='3')
plt.plot(EM2_sim.f, EM2_sim.z_im[:, 1-1, 1-1]/(EM2_sim.f*2*np.pi), label='Ind(Two)', linewidth='3')
plt.plot(TSMC_sim.f, TSMC_sim.z_im[:, 1-1, 1-1]/(TSMC_sim.f*2*np.pi), label='Ind(TSMC)', linewidth='3')
plt.grid()
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('Ind, H')

#Fitting_error(File_TSMC, File_EM1)


'''
plt.figure()
plt.plot(Two_ind.f, Two_ind.z_im[:, 2-1, 1-1], label='Z21(Two)', linewidth='3')
plt.grid()
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('Z(Im), Ом')

plt.figure()
plt.plot(Two_ind.f, Two_ind.z_re[:, 1-1, 1-1], label='Z21(Two)', linewidth='3')
plt.grid()
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('Z(Re), Ом')
'''




plt.show()