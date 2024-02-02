# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:23:09 2024

@author: Sam Lamboo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func1(x, a, b):
    """y = a * x + b"""
    return a * x + b

def func(x, a, b):
    """y = 1/a * x + b"""
    return 1/a * x + b


# Input data
wavelengths = np.array([4.9, 4.8, 4.8, 4.6, 4.5]) * 10**(-2) / 5 # In centimetres -> m
wavelength_errors = np.array([0.1, 0.1, 0.1, 0.1, 0.1]) * 10**(-2) / 5 # In centimetres -> m
frequencies = np.array([39, 39.5, 40, 40.5, 41]) * 10**(3) # In killohertz -> Hz
frequency_errors = np.zeros(np.shape(frequencies[0])) * 10**(3) # In killohertz -> Hz

# Calculate velocity
velocities = wavelengths * frequencies
velocity_errors = np.sqrt(wavelength_errors**2 * frequencies**2 + 
                          frequency_errors**2 * wavelengths)

# Plot velocity against frequency
fig, ax = plt.subplots(dpi=300)

ax.errorbar(frequencies, velocities, yerr=velocity_errors, 
            fmt='.k', capsize=2, label='measurements')
ax.set_xlabel('Frequency $f$ [Hz]')
ax.set_ylabel('Velocity $v$ [m/s]')
ax.ticklabel_format(axis='x', scilimits=(0,0))

popt, pcov = curve_fit(func1, frequencies, velocities, sigma=velocity_errors)
ax.plot(frequencies, func1(frequencies, *popt), label='linear fit')
print(popt)
print(np.sqrt(np.diag(pcov)))
ax.legend()


fig2, ax2 = plt.subplots(dpi=300)


ax2.errorbar(frequencies, wavelengths, yerr=wavelength_errors, 
            fmt='.k', capsize=2, label='measurements')
ax2.set_xlabel('Frequency $f$ [Hz]')
ax2.set_ylabel('wavelength $\\lambda$ [m]')
ax2.ticklabel_format(axis='both', scilimits=(0,0))

popt2, pcov2 = curve_fit(func1, frequencies, wavelengths, 
                         sigma=wavelength_errors)
ax2.plot(frequencies, func1(frequencies, *popt2), label='linear fit')
print(popt2)
print(np.sqrt(np.diag(pcov2)))
ax2.legend()
