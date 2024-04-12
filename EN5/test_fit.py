"""
Code written for EN5

Author: Sam Lamboo
"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def func(x, *params):
    y = np.zeros_like(x)
    for i in range(0, len(params), 3):
        mu = params[i]
        amp = params[i+1]
        sigma = params[i+2]
        y += amp * np.exp( -0.5 * ((x - mu) / sigma)**2)
    return y


filename = 'measurements/'
measurement = 'Na-D_m-1'
filename += measurement
filename += '.csv'

guess = [640, 125, 3, 660, 120, 3]

pixel, signal = np.loadtxt(filename, delimiter=',', unpack=True)

# Fit
popt, pcov = curve_fit(func, pixel, signal, p0=guess, maxfev=5000)
sigmas = np.sqrt(np.diag(pcov))
print(f'for {measurement}')
for i in range(0, len(popt), 3):
    print(f'mu_{i//3} = {popt[i]} with error {sigmas[i]}')
    print(f'amp_{i//3} = {popt[i+1]} with error {sigmas[i+1]}')
    print(f'sigma_{i//3} = {popt[i+2]} with error {sigmas[i+2]}\n')


fit = func(pixel, *popt)

# Plotting
fig, ax = plt.subplots(dpi=300)

ax.plot(pixel, signal, c='k', linewidth=1, label='measurement')
ax.plot(pixel, fit, 'r:', linewidth=1, label='fit')

ax.set_xlabel('pixel')
ax.set_ylabel('signal intensity')
ax.set_title(measurement)
ax.legend()

filename.strip('.csv')

fig.savefig(filename+'_fit.pdf')

fig.show()