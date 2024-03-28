"""
Author: Sam Lamboo

Code used for analysis in EN4
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(x, a, b):
    return 1- a * np.exp(-b*x)


zerofile = 'nulmeting'
zerofile += '_mean_fourier.csv'
boardfiles = ['1board', '2boards', '3boards', '4boards', '5boards', '6boards',
            '7boards', '8boards', '9boards', '10boards', '11boards',
            '12boards']


freq, zero, std_zero = np.loadtxt(zerofile, unpack=True)

for i, freq_index in enumerate(range(150, 201, 10)):
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
    
    thickness = (2*np.arange(1,13))
    ax.flatten()[i].errorbar(thickness, r_freq, yerr=std_r_freq, fmt='.k', capsize=2,
                label='measured damping')
    
    popt, pcov = curve_fit(func, thickness, r_freq, sigma=std_r_freq)
    perr = np.sqrt(np.diag(pcov))
    linspace = np.linspace(2, 24, 100)
    ax.plot(linspace, func(linspace, *popt),
            label=f'fit 1-({popt[0]:.1e}±{perr[0]:.0e})exp(-({popt[1]:.0e}±{perr[1]:.0e})x)')
    
    ax.set_ylim([0,1.1])
    ax.set_xlabel('thickness $d$ [cm]')
    ax.set_ylabel('damping $\\alpha$')
    ax.set_title(f'damping at {freq[freq_index]:.2f}Hz')
    ax.legend()
    
    fig.savefig(f'discrete_damping {freq[freq_index]:.0f}Hz.pdf')
    
    fig.show()