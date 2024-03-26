"""
Author: Sam Lamboo

Code used for analysis in EN4
"""

import numpy as np
import matplotlib.pyplot as plt

zerofile = 'nulmeting'
zerofile += '_mean_fourier.csv'
boardfiles = ['1board', '2boards', '3boards', '4boards', '5boards', '6boards',
            '7boards', '8boards', '9boards', '10boards', '11boards',
            '12boards']

freq, zero, std_zero = np.loadtxt(zerofile, unpack=True)

fig, ax = plt.subplots(dpi=300)
ax.set_xscale('log')


for boardname in boardfiles:
    boardfile = boardname + '_mean_fourier.csv'
    freq, board, std_board = np.loadtxt(boardfile, unpack=True)

    damping = 1 - (board/zero)
    ax.plot(freq, damping, linewidth=0.5, label=f'$\\alpha$ {boardname}')

# std_damping = np.sqrt((std_base/base)**2 + ((std_board_1*board_1)/base**2)**2)

# ax.fill_between(freq, damping+2*std_damping, damping-2*std_damping,
#                 color='r', alpha=0.2, label='2$\\sigma$')


ax.set_ylim([0, 1])


ax.set_xlabel('frequency $f$ [Hz]')
ax.set_ylabel('damping $\\alpha$')
ax.set_title('damping')
ax.legend(ncols=2, fontsize='small')

fig.show()
fig.savefig('damping_all_BAD.pdf')