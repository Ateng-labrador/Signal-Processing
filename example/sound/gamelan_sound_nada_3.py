import numpy as np
from fftModule import fft
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.io import wavfile

# data
samplerate, data = wavfile.read("nada_2.wav")
data_1 = data[100000:130000]
data_2 = data_1[0:215]
fast_fourier = fft.bluestein(data_2)

N = 215
fs = samplerate
t = np.arange(N) / fs
freq = np.arange(N) * fs / N

magnitude = 2 * np.abs(fast_fourier) / N
peaks, _ = find_peaks(magnitude, height = 10000)

plt.plot(freq, magnitude)
plt.scatter(freq[peaks], magnitude[peaks], color='red')
for p in peaks:
    plt.annotate(
            f"{freq[p]:.2f}",
            xy=(freq[p], magnitude[p]),
            xytext=(0, 8),
            textcoords="offset points",
            ha="center"
        )
plt.show()
