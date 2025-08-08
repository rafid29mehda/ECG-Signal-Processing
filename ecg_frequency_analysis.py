import numpy as np
import scipy.fft as fft
import matplotlib.pyplot as plt

# Simulate ECG signal
fs = 1000
t = np.linspace(0, 10, 10 * fs)
ecg = 0.5 * np.sin(2 * np.pi * 1 * t) + 0.1 * np.random.normal(0, 0.1, len(t))

# Compute FFT
freqs = fft.fftfreq(len(ecg), 1/fs)
fft_vals = fft.fft(ecg)
power = np.abs(fft_vals) ** 2

# Plot frequency spectrum
plt.figure(figsize=(10, 4))
plt.plot(freqs[:len(freqs)//2], power[:len(power)//2])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('ECG Frequency Spectrum')
plt.grid()
plt.show()
