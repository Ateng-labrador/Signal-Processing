# ProjectFourier - Fast Fourier Transform 

ProjectFourier is implementation of various Fast Fourier Transform (FFT)algorithms for signal analysis and 
image compression.This project provides any implementation from any FFT like Cooley-Tukey 
(Radix-2, Radix-3, Radix-4) and Bluestein, including their inverse (IFFT) for data reconstruction.

## Main Feature

- **various**: Radix-2, Radix-3, Radix-4, Cooley-Tukey, and Bluestein
- **DFT & IFFT**: Discrete Fourier transform and invers
- **FFT 2D**: support to transform image (image compression)

## Example

```python
from fftModule import fft
import numpy as np

# make simple signa
x = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=complex)

# calculation FFT using Cooley-Tukey (Radix-2)
X = fft.fft(x)
print("FFT Result:", X)

# or use Bluestein
X_bluestein = fft.bluestein(x)
print("Bluestein Result:", X_bluestein)
```

## Algorithms implementation

| Algoritma | Complexity | Note |
|-----------|--------------|--------|
| DFT | O(n²) | Direct method, slow but accurate |
| FFT (Radix-2) | O(n log n) | Cooley-Tukey, for n = 2^k |
| FFT (Radix-3/4) | O(n log n) | Cooley-Tukey variant |
| Bluestein | O(n log n) | Arbitrary size, use Cooley-Tukey internally |
| IFFT | O(n log n) | Inverse transform |
