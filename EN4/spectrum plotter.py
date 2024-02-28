# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 20:59:17 2024

@author: masla
"""

import numpy as np
import matplotlib.pyplot as plt

filename_read = 'sweep_test_home.txt'
filename_output = filename_read.strip('.txt') + '_plot.pdf'

threshold = 20000

frequency, level = np.loadtxt(filename_read, delimiter='\t', skiprows=1,
                              unpack=True)

fig, ax = plt.subplots(dpi=300)

ax.set_xscale('log')
ax.set_xlabel('Frequency $f$ [Hz]')
ax.set_ylabel('level [dB]')

ax.plot(frequency, level, c='k')

fig.show()

fig.savefig(filename_output)