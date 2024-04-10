"""
Code written for EN5

Author: Sam Lamboo
"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def func(x, *params):
    y = np.zeros_like(x)
    factor = np.sqrt(2*np.pi)
    for i in range(0, len(params), 3):
        mu = params[i]
        amp = params[i+1]
        sigma = params[i+2]
        mult = amp / (sigma*factor)
        y += mult * np.exp( -0.5 * ((x - mu) / sigma)**2)
    return y


filename = 'measurementname.csv'
guess = [633, 125, 5, 646, 120, 5]

pixel, signal = np.loadtxt(filename, delimiter=',', unpack=True)

# Fit
popt, pcov = curve_fit(func, pixel, signal, p0=guess, maxfev=5000)
print(popt)
print(np.sqrt(np.diag(pcov)))
fit = func(pixel, *popt)

# Plotting
fig, ax = plt.subplots(dpi=300)

ax.plot(pixel, signal, c='k', linewidth=1)
ax.plot(pixel, fit, 'r:', linewidth=1)

fig.show()