## Code met dank aan Meinhard

import Mydaqclass as My
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import integrate


mydaq = My.MyDAQ()

t = 1 #s
rate = 200000 #Hz
N = rate*t #total samples

time = np.linspace(0, N/rate, N)
    
voltagearray1 = np.zeros(len(time))



data = mydaq.writeread(rate, N, list(voltagearray1))

plt.plot(time,data)
plt.xlabel("Time (s)")
plt.ylabel("Voltage")
plt.title("Plot by dividing signals analog with divider circuit")
plt.show()