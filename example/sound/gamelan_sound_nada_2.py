import numpy as np
import matplotlib.pyplot as plt
from fftModule.fft import fft
from scipy.signal import find_peaks
from scipy.io import wavfile

# data
samplerate, data = wavfile.read("nada_1_rev.wav")
data_potong = data[130000:150000]
data_potong_1 = data_potong[2500:5000]
data_potong_2 = data_potong_1[2000:6000]
data_potong_3 = data_potong_2[0:500]
data_bersih = np.concatenate((data_potong_3, np.zeros(12)))
fast_fourier = fft(data_bersih)



N = 512
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
