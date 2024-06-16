# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:15:14 2024

@author: s2653346
"""

import numpy as np
import matplotlib.pyplot as plt

filename = "test_hoog_peaks.csv"

freq, fourier, noise = np.loadtxt(filename, delimiter=',', unpack=True,
                                  dtype=np.complex_)

fourier = abs(fourier)

fig, ax = plt.subplots(dpi=300)

ax2 = ax.twinx()

ax.scatter(freq, fourier, marker='.', c='k', linewidth=.1)
ax2.scatter(freq, noise, marker='.', c='r', linewidth=.1)

ax.set_xlabel("Frequency [Hz]")
ax.set_ylabel("Intensity")
ax2.set_ylabel(r"signal to 50Hz noise ratio $\frac{s}{r}$", color='r')
ax2.tick_params(axis='y', labelcolor='r')

fig.savefig('analysed_data.pdf')
fig.savefig('analysed_data.png')
fig.show()