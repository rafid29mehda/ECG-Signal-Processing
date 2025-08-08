import numpy as np
import pywt
import matplotlib.pyplot as plt

# Simulate ECG signal
fs = 1000
t = np.linspace(0, 10, 10 * fs)
ecg = 0.5 * np.sin(2 * np.pi * 1 * t) + 0.1 * np.random.normal(0, 0.1, len(t))

# Compute Continuous Wavelet Transform (CWT)
scales = np.arange(1, 128)
coeffs, freqs = pywt.cwt(ecg, scales, 'cmor1.5-1.0', sampling_period=1/fs)

# Plot
plt.figure(figsize=(10, 4))
plt.imshow(np.abs(coeffs), extent=[0, 10, 1, 128], cmap='jet', aspect='auto')
plt.colorbar(label='Amplitude')
plt.xlabel('Time (s)')
plt.ylabel('Scale')
plt.title('ECG Continuous Wavelet Transform (CWT)')
plt.show()
