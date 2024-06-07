"""
Author: Sam Lamboo

Code used for EN4 experiment
"""

import numpy as np
import matplotlib.pyplot as plt

filenamebase = 'sneltest_laatste_dag'

rate = 200000 #Hz

filename = filenamebase + '.txt'
time, data = np.loadtxt(filename, delimiter=',', unpack=True)

time = time[:200000]
data = data[:200000]


fourier = np.fft.fft(data, axis=0)

freq = np.fft.fftfreq(len(time), time[1])

fig, ax = plt.subplots(dpi=300)

ax.plot(freq, abs(fourier), c='k', linewidth=0.5)

ax.set_xlabel('frequency [Hz]')
ax.set_ylabel('intensity')

ax.legend()
ax.grid()

ax.set_xlim(0,50000)


fig.savefig(filenamebase + '.pdf')
fig.savefig(filenamebase + '.png')
ax.set_title(filenamebase)

fig.show()
