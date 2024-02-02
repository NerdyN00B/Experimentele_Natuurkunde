# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:23:09 2024

@author: Sam Lamboo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(x, a):
    """y = 1/a * x"""
    return 1/a * x


# Input data
wavelengths = np.array([0.6, 0.5, 0.6, 0.5, 0.6]) * 10**(-2) * 2 # In centimetres
wavelength_errors = np.array([0.1, 0.1, 0.1, 0.1, 0.1]) * 10**(-2) # In centimetres
frequencies = np.array([39, 39.5, 40, 40.5, 41]) * 10**(3) # In killohertz
frequency_errors = np.zeros(np.shape(frequencies[0])) * 10**(3) # In killohertz

# Calculate velocity
velocities = wavelengths * frequencies
velocity_errors = np.sqrt(wavelength_errors**2 * frequencies**2 + 
                          frequency_errors**2 * wavelengths)

# Plot velocity against frequency
fig, ax = plt.subplots(dpi=300)

ax.errorbar(frequencies, velocities, xerr=frequency_errors, 
            yerr=velocity_errors, fmt='.k', capsize=2, label='measurements')
ax.set_xlabel('Frequency $f$ [Hz]')
ax.set_ylabel('Velocity $v$ [m/s]')
ax.ticklabel_format(axis='x', scilimits=(0,0))

popt, pcov = curve_fit(func, frequencies, velocities, sigma=velocity_errors)
ax.plot(frequencies, func(frequencies, *popt))
print(popt)
print(np.sqrt(np.diag(pcov)))


fig2, ax2 = plt.subplots(dpi=300)


ax2.errorbar(frequencies, wavelengths, yerr=wavelength_errors, 
            xerr=frequency_errors, fmt='.k', capsize=2, label='measurements')
ax2.set_xlabel('Frequency $f$ [Hz]')
ax2.set_ylabel('wavelength $\\lambda$ [m]')
ax2.ticklabel_format(axis='both', scilimits=(0,0))

popt2, pcov2 = curve_fit(func, frequencies, wavelengths, 
                         sigma=wavelength_errors)
ax2.plot(frequencies, func(frequencies, *popt2))
print(popt2)
print(np.sqrt(np.diag(pcov2)))