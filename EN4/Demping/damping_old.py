"""
Author: Sam Lamboo

Code used for analysis in EN4
"""

import numpy as np
import matplotlib.pyplot as plt

basefile = 'nulmeting'
basefile += '_mean_fourier.csv'
board_1_file = '1board'
board_1_file += '_mean_fourier.csv'

freq, base, std_base = np.loadtxt(basefile, unpack=True)
freq, board_1, std_board_1 = np.loadtxt(board_1_file, unpack=True)

damping = 1 - board_1/base

std_damping = np.sqrt((std_base/base)**2 + ((std_board_1*board_1)/base**2)**2)

fig, ax = plt.subplots(dpi=300)

ax.set_xscale('log')
ax.set_ylim([0, 1])


ax.plot(freq, damping, c='k', linewidth=0.5, label='$\\alpha$ 1 board')
ax.fill_between(freq, damping+2*std_damping, damping-2*std_damping,
                color='r', alpha=0.2, label='2$\\sigma$')

ax.set_xlabel('frequency $f$ [Hz]')
ax.set_ylabel('damping $\\alpha$')
ax.set_title('damping')
ax.legend()

fig.show()
fig.savefig('Damping_1board_BAD.pdf')