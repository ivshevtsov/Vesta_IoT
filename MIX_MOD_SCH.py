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



HOME = 'DATA/MIXER/csv'
File_TOTAL = 'mix_modem_min_total.csv'



TOTAL = genfromtxt(f'{HOME}/{File_TOTAL}', delimiter=',', skip_header=1)



plt.figure()
plot_csv_hist_column(TOTAL, column=21)
plt.grid()

plt.show()