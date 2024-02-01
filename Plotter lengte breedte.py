# -*- coding: utf-8 -*-
"""
code by Sam Lamboo (s2653346)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b):
    """y = a * x^b"""
    return a * x**b


# hoogte1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 15, 25, 35, 45])
# breedte1 = np.array([29, 35, 40, 46, 49, 52, 51, 56, 36, 44, 48, 50])
# lengte1 = np.array([30, 35, 41, 46, 48, 50, 53, 55, 39, 45, 48, 50])

# verhouding1 = lengte1/breedte1

# Data + fouten
hoogte = np.array([5, 6, 8, 2, 10, 15, 20, 30, 40, 50, 65, 75, 100, 150, 200, 300])
hoogte_error = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 10, 10])
lengte = np.array([31, 34, 34, 25, 35, 40, 41, 42, 45, 50, 51, 55, 56, 60, 66, 65])
lengte_error = np.ones(lengte.shape[0])
breedte = np.array([31, 32, 35, 25, 35, 38, 40, 41, 45, 49, 52, 54, 58, 62, 66, 70])
breedte_error = np.ones(breedte.shape[0])

# Bereken verhouding en fout
verhouding = lengte/breedte
verhouding_error = np.sqrt((1/breedte)**2 * lengte_error**2 + (lengte/(breedte**2))**2 * breedte_error**2)

fig, (axL, axB, axV) = plt.subplots(1, 3, dpi=300, figsize=(10, 4), layout='tight')

# Plot!
axB.errorbar(hoogte, breedte, fmt='ok', markersize=3, yerr=breedte_error,
             xerr=hoogte_error, capsize=2, label='meetdata')
axL.errorbar(hoogte, lengte, fmt='ok', markersize=3, yerr=lengte_error,
             xerr=hoogte_error, capsize=2, label=' meetdata')
axV.errorbar(hoogte, verhouding, fmt='ok', markersize=3, yerr=verhouding_error, xerr=hoogte_error, capsize=2)

# axB.errorbar(hoogte1, breedte1, fmt='ok', markersize=3, yerr=1, xerr=1, capsize=2)
# axL.errorbar(hoogte1, lengte1, fmt='ok', markersize=3, yerr=1, xerr=1, capsize=2)
# axV.errorbar(hoogte1, verhouding1, fmt='ok', markersize=3, xerr=1, capsize=2)

# Log-assen
axL.set_yscale('log')
axL.set_xscale('log')
axB.set_yscale('log')
axB.set_xscale('log')

# Aslabels x
axL.set_xlabel('Hoogte vrije val $h$ [$cm$]')
axB.set_xlabel('Hoogte vrije val $h$ [$cm$]')
axV.set_xlabel('Hoogte vrije val $h$ [$cm$]')
# Aslabels y
axL.set_ylabel('Lengte krater $l$ [$mm$]')
axB.set_ylabel('Breedte krater $b$ [$mm$]')
axV.set_ylabel('Verhouding lengte/breedte $\\frac{l}{b}$')

# # Fitten!
gokwaarden = (1, 1/5)
popt_l, pcov_l = curve_fit(func, hoogte, lengte, gokwaarden, sigma=lengte_error)
popt_b, pcov_b = curve_fit(func, hoogte, breedte, gokwaarden, breedte_error)

# Plot fits
hoogtes = np.geomspace(1, 300, num=100)
axL.plot(hoogtes, func(hoogtes, *popt_l), c='k', label='fit')
print(f'lengtefit = {popt_l}')
print(f'met fouten = {np.sqrt(np.diag(pcov_l))}')

axB.plot(hoogtes, func(hoogtes, *popt_b), c='k', label='fit')
print(f'\nbreedtefit = {popt_b}')
print(f'met fouten = {np.sqrt(np.diag(pcov_b))}')

# Net maken en opslaan
axL.grid(which='both')
axB.grid(which='both')
axV.grid()
axL.legend()
axB.legend()

plt.savefig('analyse dv1.pdf')
