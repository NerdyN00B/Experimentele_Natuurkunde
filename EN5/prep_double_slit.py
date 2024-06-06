# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:24:01 2024

@author: Sam Lamboo (s2653346)
"""

import numpy as np
import matplotlib.pyplot as plt

def func(y, R, d, a, wavelength, I0=1):
    theta = y/R
    beta = np.pi * a * theta / wavelength
    alpha = np.pi * d / wavelength * theta
    sinc2 = np.sinc(beta)**2
    cos2 = np.cos(alpha)**2
    return I0 * sinc2 * cos2, sinc2

y = np.linspace(-5e-2, 5e-2, 5000)

fig, ax = plt.subplots(dpi=300)

values, envelope = func(y, 10e-2, 2e-5, 2e-6, 698e-9)

ax.plot(y, values, c='#ff0000', linewidth=1, label='wavelength: 698nm')
ax.plot(y, envelope, c='k', ls='--', linewidth=1, label='envelope')

ax.set_xlabel('y [$m$]')
ax.set_ylabel('I [$I_0$]')
ax.legend()

fig.savefig('double_slit.pdf')
fig.show()
