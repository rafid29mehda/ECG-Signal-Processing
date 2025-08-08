import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Simulate ECG signal
fs = 1000
t = np.linspace(0, 10, 10 * fs)
ecg = 0.5 * np.sin(2 * np.pi * 1 * t) + 0.1 * np.random.normal(0, 0.1, len(t))

# Compute Power Spectral Density (PSD)
freqs, psd = signal.welch(ecg, fs=fs, nperseg=1024)

# Plot
plt.figure(figsize=(10, 4))
plt.semilogy(freqs, psd)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (V^2/Hz)')
plt.title('ECG Power Spectral Density')
plt.xlim(0, 50)
plt.grid()
plt.show()
