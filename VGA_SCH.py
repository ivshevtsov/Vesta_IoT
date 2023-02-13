import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import scipy.stats as st

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


def plot_csv_column(data, column_x, column_y, xlabel, ylabel, percent):
    len_data = int(len(data[:, column_x-1])*percent/100)
    plt.plot(data[:len_data, column_x-1], data[:len_data, column_y-1], linewidth='2')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def plot_csv_hist_column(data, column):

    plt.hist(data[:, column-1], density=True,  facecolor='g')
    mn, mx = plt.xlim()
    plt.xlim(mn, mx)
    kde_xs = np.linspace(mn, mx, 300)
    kde = st.gaussian_kde(data[:, column-1])
    plt.plot(kde_xs, kde.pdf(kde_xs), label="PDF")
    mu = np.mean(data[:, column-1])
    std = np.std(data[:, column-1])
    #plt.title(fr'$\mu$={round(mu/1e6, 2)}МГц, $\sigma$={round(std/1e3, 2)}кГц')
    #plt.title(fr'$\mu$={round(mu, 2)}дБ, $\sigma$={round(std, 2)}дБ')
    plt.title(fr'$\mu$={round(mu*1000, 2)}мВ, $\sigma$={round(std*1000, 2)}мВ')
    plt.ylabel('Probability')
    '''
    plt.figure()
    plt.ylabel(fr'$\sigma$')
    plt.xlabel(fr'N')
    print(len(data[:, column - 1]))
    for i in range(len(data[:, column - 1])):
        # require give list for histogramm
        plt.plot(i, np.std(data[:i + 1, column - 1]), '.', linewidth='2')
    '''



HOME = 'DATA/VGA/csv'
File_TOTAL = 'vga_total_max_sch.csv'
File_reg = 'vga_reg_max.csv'
File_step_dm = 'vga_step_dm.csv'
File_step_cm = 'vga_step_cm.csv'

REG = genfromtxt(f'{HOME}/{File_reg}', delimiter=',', skip_header=1)
TOTAL = genfromtxt(f'{HOME}/{File_TOTAL}', delimiter=',', skip_header=1)
STEP_DM = genfromtxt(f'{HOME}/{File_step_dm}', delimiter=',', skip_header=1)
STEP_CM = genfromtxt(f'{HOME}/{File_step_cm}', delimiter=',', skip_header=1)

# plot reg gain
plt.figure()
plot_csv_column(REG, column_x=1, column_y=2, xlabel='N', ylabel='Gain, дБ', percent=100)
plt.grid()

# plot reg band
plt.figure()
plot_csv_column(REG, column_x=1, column_y=3, xlabel='N', ylabel='Band, Гц', percent=100)
plt.grid()

# plot step dm
plt.figure()
plot_csv_column(STEP_DM, column_x=1, column_y=2, xlabel='t, c', ylabel='A, В', percent=100)
plt.grid()

# plot step сm
plt.figure()
plot_csv_column(STEP_CM, column_x=1, column_y=2, xlabel='t, c', ylabel='A, В', percent=100)
plt.grid()




'''

# plot HF
plt.figure()
plot_csv_column(PVT, column_x=1, column_y=2, xlabel='f, Гц', ylabel='HF, дБ', percent=60)
plt.grid()

# plot GD
plt.figure()
plot_csv_column(PVT, column_x=3, column_y=4, xlabel='f, Гц', ylabel='GD, с', percent=60)
plt.grid()

# plot NF
plt.figure()
plot_csv_column(PVT, column_x=5, column_y=6, xlabel='f, Гц', ylabel='NF, дБ', percent=100)
plt.grid()


'''

plt.figure()
plot_csv_hist_column(TOTAL, column=12)
plt.grid()

plt.show()