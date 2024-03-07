"""
Author: Sam Lamboo

Code used for EN4 experiment
"""

import numpy as np
import matplotlib.pyplot as plt

filenamebase = '1board'
ammount = 5

t = 2 #s
rate = 200000 #Hz
time = np.linspace(0, t, rate*t)


data = []
for i in range(ammount):
    filename = filenamebase + f'_{i}.csv'
    data.append(np.loadtxt(filename))

data_all = np.asarray(data)


fourier = []
for i in range(ammount):
    fourier.append(np.fft.fft(data_all[i], axis=0))

fourier_all = np.asarray(fourier)

freq = np.fft.fftfreq(rate*t, time[1])

mean_fourier = np.mean(np.absolute(fourier), axis=0)
std_fourier = np.std(np.absolute(fourier), axis=0)

fig, ax = plt.subplots(dpi=300)

freqslice = np.logical_and(freq >= 300, freq <= 15000)

freq = freq[freqslice]
mean_fourier = mean_fourier[freqslice]
std_fourier = std_fourier[freqslice]

ax.set_xscale('log')
ax.plot(freq, mean_fourier, c='k', linewidth=0.5, label='mean spectrum')

ax.fill_between(freq, mean_fourier+2*std_fourier, mean_fourier-2*std_fourier,
                color='r', alpha=0.2, label='2$\\sigma$')

ax.set_xlabel('frequency [Hz]')
ax.set_ylabel('intensity')
ax.set_title(filenamebase)

ax.legend()

fig.show()
fig.savefig(filenamebase + '.pdf')
fig.savefig(filenamebase + '.png')

np.savetxt(filenamebase + f'_mean_fourier.csv', 
           np.c_[freq, mean_fourier, std_fourier],
           header='# Frequency, Mean Fourier, std fourier')
