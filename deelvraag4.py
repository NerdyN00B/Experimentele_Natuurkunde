# -*- coding: utf-8 -*-
"""
Code by Sam Lamboo (s2653346)
"""

import numpy as np
import matplotlib.pyplot as plt

# Init dicts
hoogte = {}
hoogte_error = {}
lengte = {}
lengte_error = {}
breedte = {}
breedte_error = {}
hoeken = {}
hoeken_error = {}

verhouding = {}
verhouding_error = {}


# Data + fouten Voor 90deg
hoek = 90
hoogte[90] = np.array([5, 6, 8, 2, 10, 15, 20, 30, 40, 50, 65, 75, 100, 150, 200, 300])
hoogte_error[90] = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 10, 10])
lengte[90] = np.array([31, 34, 34, 25, 35, 40, 41, 42, 45, 50, 51, 55, 56, 60, 66, 65])
lengte_error[90] = np.ones(lengte[90].shape[0])
breedte[90] = np.array([31, 32, 35, 25, 35, 38, 40, 41, 45, 49, 52, 54, 58, 62, 66, 70])
breedte_error[90] = np.ones(breedte[90].shape[0])
hoeken[hoek] = hoek * np.ones(hoogte[hoek].shape[0])
hoeken_error[hoek] = 0 * np.ones(hoeken[hoek].shape[0])

# Data + fouten 65deg
hoek = 65
hoogte[hoek] = np.array([5, 25, 80])
hoogte_error[hoek] = 2 * np.ones(hoogte[hoek].shape[0])
lengte[hoek] = np.array([29, 47, 58])
lengte_error[hoek] = np.ones(lengte[hoek].shape[0])
breedte[hoek] = np.array([27, 47, 60])
breedte_error[hoek] = np.ones(breedte[hoek].shape[0])
hoeken[hoek] = hoek * np.ones(hoogte[hoek].shape[0])
hoeken_error[hoek] = 3 * np.ones(hoeken[hoek].shape[0])

# Data + fouten 60deg
hoek = 60
hoogte[hoek] = np.array([5, 25, 90])
hoogte_error[hoek] = 2 * np.ones(hoogte[hoek].shape[0])
lengte[hoek] = np.array([30, 44, 57])
lengte_error[hoek] = np.ones(lengte[hoek].shape[0])
breedte[hoek] = np.array([31, 41, 57])
breedte_error[hoek] = np.ones(breedte[hoek].shape[0])
hoeken[hoek] = hoek * np.ones(hoogte[hoek].shape[0])
hoeken_error[hoek] = 3 * np.ones(hoeken[hoek].shape[0])

# Data + fouten 55deg
hoek = 55
hoogte[hoek] = np.array([5, 25, 100])
hoogte_error[hoek] = 2 * np.ones(hoogte[hoek].shape[0])
lengte[hoek] = np.array([30, 48, 64])
lengte_error[hoek] = np.ones(lengte[hoek].shape[0])
breedte[hoek] = np.array([31, 45, 65])
breedte_error[hoek] = np.ones(breedte[hoek].shape[0])
hoeken[hoek] = hoek * np.ones(hoogte[hoek].shape[0])
hoeken_error[hoek] = 3 * np.ones(hoeken[hoek].shape[0])

# Data + fouten 50deg
hoek = 50
hoogte[hoek] = np.array([5, 25, 96])
hoogte_error[hoek] = 2 * np.ones(hoogte[hoek].shape[0])
lengte[hoek] = np.array([40, 56, 75])
lengte_error[hoek] = np.ones(lengte[hoek].shape[0])
breedte[hoek] = np.array([34, 48, 60])
breedte_error[hoek] = np.ones(breedte[hoek].shape[0])
hoeken[hoek] = hoek * np.ones(hoogte[hoek].shape[0])
hoeken_error[hoek] = 3 * np.ones(hoeken[hoek].shape[0])

# Data + fouten voor 45deg
hoek = 45
hoogte[45] = np.array([2, 5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 80, 85])
hoogte_error[45] = 2*np.ones(hoogte[45].shape[0])
lengte[45] = np.array([32, 36, 44, 46, 52, 50, 53, 62, 62, 67, 66, 72, 71])
lengte_error[45] = np.ones(lengte[45].shape[0])
breedte[45] = np.array([27, 33, 39, 41, 38, 42, 49, 53, 54, 56, 58, 64, 65])
breedte_error[45] = np.ones(breedte[45].shape[0])
hoeken[hoek] = hoek * np.ones(hoogte[hoek].shape[0])
hoeken_error[hoek] = 5 * np.ones(hoeken[hoek].shape[0])

# Data + fouten 40deg
hoek = 40
hoogte[hoek] = np.array([5, 25, 100, 10])
hoogte_error[hoek] = 2 * np.ones(hoogte[hoek].shape[0])
lengte[hoek] = np.array([39, 74, 94, 42])
lengte_error[hoek] = np.ones(lengte[hoek].shape[0])
breedte[hoek] = np.array([26, 38, 57, 36])
breedte_error[hoek] = np.ones(breedte[hoek].shape[0])
hoeken[hoek] = hoek * np.ones(hoogte[hoek].shape[0])
hoeken_error[hoek] = 3 * np.ones(hoeken[hoek].shape[0])

# Data + fouten 35deg
hoek = 35
hoogte[hoek] = np.array([5, 25, 100])
hoogte_error[hoek] = 2 * np.ones(hoogte[hoek].shape[0])
lengte[hoek] = np.array([45, 72, 108])
lengte_error[hoek] = np.ones(lengte[hoek].shape[0])
breedte[hoek] = np.array([31, 43, 59])
breedte_error[hoek] = np.ones(breedte[hoek].shape[0])
hoeken[hoek] = hoek * np.ones(hoogte[hoek].shape[0])
hoeken_error[hoek] = 3 * np.ones(hoeken[hoek].shape[0])

# Data + fouten 30deg
hoek = 30
hoogte[hoek] = np.array([5, 25, 50])
hoogte_error[hoek] = 2 * np.ones(hoogte[hoek].shape[0])
lengte[hoek] = np.array([48, 91, 100])
lengte_error[hoek] = np.ones(lengte[hoek].shape[0])
breedte[hoek] = np.array([31, 38, 50])
breedte_error[hoek] = np.ones(breedte[hoek].shape[0])
hoeken[hoek] = hoek * np.ones(hoogte[hoek].shape[0])
hoeken_error[hoek] = 3 * np.ones(hoeken[hoek].shape[0])

# Data + fouten 20deg
hoek = 20
hoogte[20] = np.array([2, 5, 10, 20, 30, 50])
hoogte_error[20] = 2 * np.ones(hoogte[20].shape[0])
lengte[20] = np.array([39, 64, 84, 127, 14, 220])
lengte_error[20] = np.ones(lengte[20].shape[0])
breedte[20] = np.array([22, 27, 30, 35, 39, 38])
breedte_error[20] = np.ones(breedte[20].shape[0])
hoeken[hoek] = hoek * np.ones(hoogte[hoek].shape[0])
hoeken_error[hoek] = 2 * np.ones(hoeken[hoek].shape[0])


# Bereken verhouding + error
for k in lengte.keys():
    verhouding[k] = lengte[k]/breedte[k]

for k in lengte.keys():
    verhouding_error[k] = (1/breedte[k])**2 * lengte_error[k]**2 
    verhouding_error[k] += (lengte[k]/(breedte[k]**2))**2 * breedte_error[k]**2
    verhouding_error[k] = np.sqrt(verhouding_error[k])


# Maak plotjes
fig, ax = plt.subplots(5, 2, dpi=300, layout='tight', figsize=(10, 20))

v1 = 0
v2 = 0

for i, k in enumerate(lengte.keys()):
    if i%2 == 0:
        ax[v1, 0].errorbar(hoogte[k], verhouding[k], xerr=hoogte_error[k],
                       yerr=verhouding_error[k], fmt='ok', capsize=2)
        ax[v1, 0].set_title(f"Verhouding {k} graden")
        ax[v1, 0].set_xlabel("Hoogte $h$ [$cm$]")
        ax[v1, 0].set_ylabel("Verhouding $\\frac{l}{b}$")
        v1 += 1
    
    else:
        ax[v2, 1].errorbar(hoogte[k], verhouding[k], xerr=hoogte_error[k],
                       yerr=verhouding_error[k], fmt='ok', capsize=2)
        ax[v2, 1].set_title(f"Verhouding {k} graden")
        ax[v2, 1].set_xlabel("Hoogte $h$ [$cm$]")
        ax[v2, 1].set_ylabel("Verhouding $\\frac{l}{b}$")
        v2 += 1

fig.savefig('deelvraag 4 plot per hoek.pdf')

fig, ax = plt.subplots(dpi=300)

for hoek in hoeken.keys():
    if hoek >= 45:
        plt.errorbar(hoeken[hoek], verhouding[hoek], xerr=hoeken_error[hoek],
                    yerr=verhouding_error[hoek], fmt='ok', capsize=2)

ax.invert_xaxis()
ax.grid()
ax.set_xlabel("Hoek $\\theta$ [$^{\\circ}$]")
ax.set_ylabel("Verhouding $\\frac{l}{b}$")

fig.savefig("Deelvraag 4 hoek tov verhouding.pdf")
