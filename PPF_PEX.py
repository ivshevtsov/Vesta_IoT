import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import scipy.stats as st

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


def plot_csv_column(data, column_x, column_y, xlabel, ylabel, percent):
    len_data = int(len(data[:, column_x-1])*percent/100)
    plt.plot(data[:len_data, column_x-1], -data[:len_data, column_y-1]+1.5, linewidth='2')
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
    plt.title(fr'$\mu$={round(mu/1e6, 2)}МГц, $\sigma$={round(std/1e3, 2)}кГц')
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


HOME = 'DATA/PPF_PEX/csv'
File_PVT = 'ppf_lpf_pvt_pex_plot.csv'
File_step_dm = 'ppf_lpf_step_dm_pex.csv'

PVT = genfromtxt(f'{HOME}/{File_PVT}', delimiter=',', skip_header=1)
STEP_DM = genfromtxt(f'{HOME}/{File_step_dm}', delimiter=',', skip_header=1)

# plot HF
plt.figure()
plot_csv_column(PVT, column_x=3, column_y=4, xlabel='f, Гц', ylabel='HF, дБ', percent=100)
plt.xscale('log')
plt.grid()

# plot GD
plt.figure()
plot_csv_column(PVT, column_x=1, column_y=2, xlabel='f, Гц', ylabel='GD, с', percent=100)
plt.grid()

# plot NF
plt.figure()
plot_csv_column(PVT, column_x=5, column_y=6, xlabel='f, Гц', ylabel='NF, дБ', percent=100)
plt.grid()

# plot step dm
plt.figure()
plot_csv_column(STEP_DM, column_x=1, column_y=2, xlabel='t, c', ylabel='U, В', percent=100)
plt.grid()

plt.show()