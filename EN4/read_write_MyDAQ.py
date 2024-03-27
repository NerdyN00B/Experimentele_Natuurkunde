"""
Code voor uitlezen MyDAQ met dank aan Meinhard

Aangepast voor metingen door Sam Lamboo
"""
import Mydaqclass as My
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import integrate

savepath = 'P:\EN4\Daadwerkelijke_metingen\\'
savefile = input('hoe wil je de datafile noemen? (zonder extension)\n')

def sweep(time, vpp=7, start=300, stop=15000):
    amplitude = vpp / 2
    frequency_difference = stop - start
    linear_frequency = start + (frequency_difference / time[-1]) * time
    offset = 0 
    return offset + amplitude * np.sin(2 * np.pi * linear_frequency * time)



mydaq = My.MyDAQ()

t = 2 #s
rate = 200000 #Hz
N = rate*t #total samples

time = np.linspace(0, N/rate, N)

audio_sweep = sweep(time, start=300, stop=15000)

audio_sweep[-1] = 0

voltagearray1 = np.linspace(0,1,N)


iters = 5

fig, ax = plt.subplots(layout='tight')

ax.set_xscale('log')
ax.axis(ymin=None, ymax=2500, xmin=200, xmax=16000)

for i in range(iters):
    print(f"measurement {i}")
    data = mydaq.writeread(rate, N, audio_sweep)
    
    np.savetxt(savepath + savefile + f'_{i}'+'.csv', np.c_[data, time],
               delimiter=',')
    
    fourier = np.fft.fft(data)
    frequencies = np.fft.fftfreq(time.size, time[1]-time[0])
    
    ax.plot(frequencies, np.abs(fourier), label=savefile + f'_{i}')


ax.set_xlabel("Frequency [Hz]")
ax.set_ylabel("Intensity")
ax.set_title(savefile)
ax.legend()
fig.savefig(savepath + savefile + '.png')
fig.show()
