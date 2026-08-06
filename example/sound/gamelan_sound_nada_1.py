import numpy as np
from fftModule import fft
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.io import wavfile

# data
samplerate, data = wavfile.read("nada_1.wav")
data_potong = data[120000:150000]
data_bersih = data_potong[0:512]
fast_fourier = fft.fft(data_bersih)

N = 512
fs = 512
t = np.arange(N) / fs
freq = np.arange(N) * fs / N

magnitude = 2 * np.abs(fast_fourier) / N
peaks, _ = find_peaks(magnitude, height = 1000)

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
