import numpy as np
import matplotlib.pyplot as plt


def sweep(time, vpp=7, start=300, stop=15000):
    amplitude = vpp/2
    frequency_difference = stop - start
    linear_frequency = 300 + (frequency_difference / time[-1]) * time
    offset = 0 + amplitude
    return offset + amplitude * np.sin(2 * np.pi * linear_frequency * time)



t = 1 #s
rate = 200000 #Hz
N = rate*t #total samples

time = np.linspace(0, N/rate, N)

audio_sweep = sweep(time)

fourier = np.fft.fft(audio_sweep)
frequencies = np.fft.fftfreq(time.size, time[1]-time[0])

plt.plot(frequencies, np.abs(fourier))
plt.xlim(300, 16000)
plt.ylim(0, 3000)
plt.show()