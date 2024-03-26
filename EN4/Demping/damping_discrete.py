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

for freq_index in range(0, 100, 10):
    fig, ax = plt.subplots(dpi=300)
    
    r_freq = []
    std_r_freq = []
    
    for boardname in boardfiles:
        boardfile = boardname + '_mean_fourier.csv'
        freq, board, std_board = np.loadtxt(boardfile, unpack=True)
    
        damping = 1 - (board/zero)
        std_damping = np.sqrt((std_zero/zero)**2 + ((std_board*board)/zero**2)**2)
        
        r_freq.append(damping[freq_index])
        std_r_freq.append(std_damping[freq_index])
    
    
    ax.errorbar(np.arange(1, 13), r_freq, yerr=std_r_freq, fmt='.k', capsize=2)
    
    
    ax.set_xlabel('boards')
    ax.set_ylabel('damping $\\alpha$')
    ax.set_title(f'damping at {freq[freq_index]:.2f}Hz')
    ax.legend()
    
    fig.show()