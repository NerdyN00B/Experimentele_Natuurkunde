"""
Code voor uitlezen MyDAQ met dank aan Meinhard

Aangepast voor metingen door Sam Lamboo
"""
import Mydaqclass as My
import numpy as np
import matplotlib.pyplot as plt

savepath = 'P:\EN6\Daadwerkelijke_metingen\\'
savefile = 'automated_measurement'

def sine(time, vpp=15, frequency=40000, offset=0):
    """Generate a sine wave with the given parameters.
    
    Parameters
    ----------
    time : array_like
        Time values at which the sine wave is evaluated.
    vpp : float, optional
        Peak-to-peak voltage of the sine wave.
    frequency : float, optional
        Frequency of the sine wave in Hz.
    offset : float, optional
        Offset of the sine wave in volts.
    
    Returns
    -------
    array_like
        intensity of sinewave with given parameters. The last value is set to 0
        in order for the mydaq to end properly.
        """
    amplitude = vpp / 2
    wave = offset + amplitude * np.sin(2 * np.pi * frequency * time)
    wave[-1] = 0
    return wave


mydaq = My.MyDAQ()

t = 1 #s
rate = 200000 #Hz
N = rate*t #total samples

f_start = 30000 #Hz
f_stop = 50000 #Hz
steps = 80

frequencies = np.linspace(f_start, f_stop, steps+1).astype(int)

time = np.linspace(0, t, N)

fig, ax = plt.subplots(layout='tight')

ax.axis(ymin=None, ymax=None, xmin=0, xmax=50000)

closest_freq = []
found_fourier = []
signal_to_noise = []
for frequency in frequencies:
    print(f"measuring at {frequency} Hz")
    data = mydaq.writeread(rate, N, sine(time, frequency=frequency))
    
    print("Saving data and analysing...")
    np.savetxt(savepath + savefile + f'_{frequency}Hz'+'.csv',
               np.c_[time, data],
               header='#column 1: Time, column 2: Voltage',
               delimiter=',')
    
    fourier = np.fft.fft(data)
    freq = np.fft.fftfreq(time.size, time[1]-time[0])

    index = np.argmin(np.abs(freq - frequency))
    index_50 = np.argmin(np.abs(freq - 50))

    closest_freq.append(freq[index])
    found_fourier.append(fourier[index])

    signal_to_noise.append(np.abs(fourier[index]) / np.abs(fourier[index_50]))

    ax.plot(freq, np.abs(fourier), label=savefile + f'_{i}')

peaks = np.c_[closest_freq, found_fourier, signal_to_noise]

np.savetxt(savepath + savefile + f'_peaks' + '.csv',
           peaks,
           header='#column 1: frequency, column 2: fourier intensity, column 3: signal to noise ratio at 50Hz',
           delimiter=',')

ax.set_xlabel("Frequency [Hz]")
ax.set_ylabel("Intensity")
ax.set_title(savefile)
ax.legend()
fig.savefig(savepath + savefile + '.png')
fig.show()
