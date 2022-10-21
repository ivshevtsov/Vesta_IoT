import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from math import log10
from cmath import phase
import skrf as rf

#calculate number strings and colums
#return mas[string, colums]
def n_string_colums(File, dot = ','):
    comment = ["#", ";"]
    num_colums = 0
    num_strings = 0
    # Size of massive
    with open(File) as Read:
        for line in Read:
            string = line
            if string[0] != comment[0] and string[0] != comment[1] and string[0].isalpha() != True:
                num_colums = len(line.split(","))
                num_strings = num_strings + 1
    string_colum = [num_strings, num_colums]
    return string_colum

#read random file from simulation
#return mas[i,j]

def read_file(File, dot = ',', Text = ''):
    comment = ["#", ";"]
    Size = n_string_colums(File)
    mas = []
    Value_1 = np.zeros((Size[0], Size[1]))
    i=0

    #Write massive
    with open(File) as Read:
        for line in Read:
            string  = line
            if  string[0] != comment[0] and string[0] != comment[1] and string[0].isalpha() != True:
                mas = line.split(dot)
                for k in range(Size[1]):
                    Value_1[i, k] = float(mas[k])
                i=i+1
    print(f'Число столбцов {Text}= {Size[1]}')
    print(f'Число строк {Text}= {Size[0]}')
    return Value_1


#plot with two y labels
def plot_two_y(F, First, Second, label_first, label_second, xlabel):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    #axis one
    color = 'tab:red'
    ax1.plot(F, First, color = color, linewidth=3)
    ax1.set_ylabel(label_first, color = color)
    ax1.set_xlabel(xlabel)
    ax1.grid()
    #axis two
    color ='tab:blue'
    ax2.plot(F, Second, color=color, linewidth=3)
    ax2.set_ylabel(label_second, color=color)
    plt.xscale('log')

#calculate stepen of ten
def stepen(k):
    i = 0
    if k >= 10:
        while k > 1:
            k = k / 10
            i = i + 1
    else:
        i = 0.1
    return i

#Calculate polinom for plot
def poly_from_file(File_poles, File_zeros, from_x, to_x, N_point):

    #Poles and zeros files
    Poles = read_file(File_poles, Text='Poles')
    Size_File_pole = n_string_colums(File_poles)
    Zeros = read_file(File_zeros, Text='Zeros')
    Size_File_zero = n_string_colums(File_zeros)

    F = np.logspace(stepen(from_x), stepen(to_x), N_point, endpoint=True)
    POLINOM = np.zeros([len(F), 2], complex)

    for i in range(len(F)):

        # Poles
        Denominator = 1
        for string in range(Size_File_pole[0]):
            sigma_p = -(Poles[string, 1] / (2 * Poles[string, 0]))
            omega_p = sqrt(pow(Poles[string, 1], 2) - pow(sigma_p, 2))
            c_Pole = complex(sigma_p, omega_p)
            Denominator = Denominator * (1 - complex(0, F[i]) / c_Pole)

        # Zeros
        Numerator = 1
        counter = 0
        for string in range(Size_File_zero[0]):
            counter = counter + 1
            if Zeros[string, 0] == 0.5 or Zeros[string, 0] == -0.5:
                sigma_z = -(Zeros[string, 1] / (2 * Zeros[string, 0]))
                omega_z = sqrt(pow(Zeros[string, 1], 2) - pow(sigma_z, 2))
                c_Zero = complex(sigma_z, omega_z)
            else:
                k = pow(-1, counter)
                sigma_z = -(Zeros[string, 1] / (2 * abs(Zeros[string, 0])))
                omega_z = sqrt(pow(Zeros[string, 1], 2) - pow(sigma_z, 2))
                c_Zero = complex(sigma_z, omega_z * k)
            Numerator = Numerator * (1 - complex(0, F[i]) / c_Zero)

        # Poly
        POLINOM[i, 1] = Numerator / Denominator
        POLINOM[i, 0] = F[i]

    return POLINOM

#calculate db values of polynom
def poly_db(Massive):
    Polinom_db = np.zeros([len(Massive), 2], float)

    for i in range(len(Massive)):
        #db Value
        Polinom_db[i, 1] = 20 * log10(abs(Massive[i, 1]))
        #Frequency
        Polinom_db[i, 0] = Massive[i, 0].real
    return Polinom_db


#calculate deg Values of polynom
def poly_deg(Massive):
    Polinom_phase = np.zeros([len(Massive), 2], float)
    flag_phase = 0
    for i in range(len(Massive)):
        # Phase
        if flag_phase == 0:
            Polinom_phase[i, 1] = phase(Massive[i, 1]) * 180 / 3.14
        else:
            Polinom_phase[i, 1] = phase(Massive[i, 1]) * 180 / 3.14 - 360
        if Polinom_phase[i, 1] <= -179:
            flag_phase = 1
    # Frequency
    Polinom_phase[i, 0] = Massive[i, 0].real

    return Polinom_phase


def pole_zero_plot(p, z, color_p='Tab:red', color_z='Tab:blue',
                   legend_p='poles', legend_z='zeros'):
    plt.figure()
    #for i in range(len(p)):
    # plot poles/zeros
    plt.scatter(p.real, p.imag, s=150, marker='*', c=color_p, label=legend_p)
    plt.scatter(z.real, z.imag, s=30, marker='o', c=color_z, label=legend_z )
    plt.grid(which='both', axis='both')
    plt.xlabel('Real')
    plt.ylabel('Imag')

def pole_plot(p, color_p='Tab:red', legend_p='poles'):
    plt.scatter(p.real, p.imag, s=150, marker='*', c=color_p, label=legend_p)







#plot pole/zero. Calculate Q/F for design
def Butterworth_pole_zero(Order, Freq, p, z):
    Order_half = int(Order)/2
    print(f'Filter Order N = {Order}')
    pole_zero_plot(p, z, color_p='Tab:red', color_z='Tab:blue')
    for i in range(len(p)):
        # calculate quality factor and normalized F
        Q = -abs(p[i]) / (2 * p[i].real)
        F = abs(p[i]) / Freq

        # parameters of blocks
        if Order % 2 != 0:
            if i <int(Order_half) :
                print(f'#-- Block {i + 1} --#')
                print(f'Pole: {round(p[i] ,4)}')
                print(f'Second order block Q = {round(Q, 4)}')
                print(f'Normalized Freq = {round(F, 4)}')
            elif i == int(Order_half):
                print(f'#-- Block {i + 1} --#')
                print(f'Pole: {round(p[i], 4)}')
                print(f'First order block Q = {round(Q, 4)}')
                print(f'Normalized Freq = {round(F, 4)}')
        else:
            if i < int(Order_half):
                print(f'#-- Block {i + 1} --#')
                print(f'Pole: {round(p[i], 4)}')
                print(f'Second order block Q = {round(Q, 4)}')
                print(f'Normalized Freq = {round(F, 4)}')


def PLOT_s_db_Dir(Directory, label='Test', N_fig = 1, sp = 11):
    Data = rf.Network(Directory)
    plt.figure(N_fig)
    First = int(sp/10)
    Second = sp - First*10
    Data.plot_s_db(m=First - 1, n=Second - 1, label=label, linewidth='3')
    plt.ylabel(f'S{sp}, дБ')
    plt.xlabel('F, Гц')


def PLOT_s_db_Netw(Network, label='Test', N_fig = 1, sp = 11):
    plt.figure(N_fig)
    First = int(sp/10)
    Second = sp - First*10
    Network.plot_s_db(m=First - 1, n=Second - 1, label=label, linewidth='3')
    plt.ylabel(f'S{sp}, дБ')
    plt.xlabel('F, Гц')

#read and create massive from cadence
def read_pole_zeros_cadence(Directory):
    Value_1 =read_file(Directory)
    N_elements = len(Value_1[:, 0])
    poles = np.zeros(N_elements, complex)

    for i in range(N_elements):
        sigma_p = -(Value_1[i, 1] / (2 * Value_1[i, 0]))
        omega_p = np.sqrt(pow(Value_1[i, 1], 2) - pow(sigma_p, 2))
        if i <N_elements-1 and  Value_1[i, 0] == Value_1[i+1, 0]:
            c_Pole = complex(sigma_p, -omega_p)
        else:
            c_Pole = complex(sigma_p, omega_p)
        poles[i]=c_Pole
        print(poles[i])
    return poles