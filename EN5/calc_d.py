# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:29:40 2024

@author: s2653346
"""
import numpy as np


def func(m, wl, alpha, sigma_alpha):
    teller = m * wl * np.cos(alpha) * sigma_alpha
    noemer = np.sin(alpha)**2
    return np.abs(teller / noemer)

def calc_d(m, wl, alpha):
    return (m*wl)/np.sin(alpha)


wl1 = 588.9950954e-9
wl2 = 589.5824237e-9

m = np.asarray([-1, -1, 1, 1, 2, 2])
wl = np.asarray([wl2, wl1, wl1, wl2, wl1, wl2])
alpha = np.asarray([-(20 + 25/60), -(20 + 24/60), 20 + 20/60, 20 + 22/60,
                    45 + 44/60, 45 + 46/60])

sigma_d = func(m, wl, np.radians(alpha), 2/60)

d = calc_d(m, wl, np.radians(alpha))

print(d)
print(f'The mean d = {np.mean(d)}')
print(f'Sigma d = {np.std(d)}')