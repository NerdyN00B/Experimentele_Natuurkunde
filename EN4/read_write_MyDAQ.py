## Code met dank aan Meinhard

import Mydaqclass as My
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import integrate


savefile = input('hoe wil je de datafile noemen? (zonder extension)\n')
savefile += '.csv'


def sweep(time, vpp=7, start=300, stop=15000):
    amplitude = vpp/2
    frequency_difference = stop - start
    linear_frequency = 300 + (frequency_difference / time[-1]) * time
    offset = 0 + amplitude
    return offset + amplitude * np.sin(2 * np.pi * linear_frequency * time)



mydaq = My.MyDAQ()

t = 1 #s
rate = 200000 #Hz
N = rate*t #total samples

time = np.linspace(0, N/rate, N)

audio_sweep = sweep(time)
    
voltagearray1 = np.zeros(len(time))


data = mydaq.writeread(rate, N, list(audio_sweep))

np.savetxt(savefile, data, delimiter=',')

plt.plot(time,data)
plt.xlabel("Time (s)")
plt.ylabel("Voltage")
plt.title("Plot by dividing signals analog with divider circuit")
plt.show()