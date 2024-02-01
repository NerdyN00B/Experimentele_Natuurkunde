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
wavelengths = np.array([1, 2]) * 10**(-2) # In centimetres
wavelength_errors = np.array([1, 1]) * 10**(-2) # In centimetres
frequencies = np.array([1, 2]) * 10**(3) # In killohertz
frequency_errors = np.array([1, 1]) * 10**(3) # In killohertz

# Calculate velocity
velocities = wavelengths * frequencies
velocity_errors = np.sqrt(wavelength_errors**2 * frequencies**2 + 
                          frequency_errors**2 * wavelengths)

# Plot velocity against frequency
fig, ax = plt.subplots(dpi=300)

ax.errorbar(frequencies, velocities, xerr=frequency_errors, 
            yerr=velocity_errors, fmt='.k', capsize=2)

popt, pcov = curve_fit(func, frequencies, velocities, sigma=velocity_errors)
ax.plot(frequencies, func(frequencies, *popt))
print(popt)
print(np.sqrt(np.diag(pcov)))


fig2, ax2 = plt.subplots(dpi=300)


ax2.errorbar(frequencies, wavelengths, xerr=wavelength_errors, 
            yerr=velocity_errors, fmt='.k', capsize=2)

popt2, pcov2 = curve_fit(func, frequencies, wavelengths, 
                         sigma=wavelength_errors)
ax2.plot(frequencies, func(frequencies, *popt))
print(popt2)
print(np.sqrt(np.diag(pcov2)))