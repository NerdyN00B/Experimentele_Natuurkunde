"""
Author: Sam Lamboo

Code used for EN4 experiment
"""

import numpy as np
import matplotlib.pyplot as plt

filenamebase = 'nulmeting'
ammount = 10

data = []
for i in range(ammount):
    filename = filenamebase + f'_{i}'
    data.append(np.readtxt(filename))
