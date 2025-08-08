import numpy as np
import pywt
import matplotlib.pyplot as plt

# Simulate ECG with noise
fs = 1000
t = np.linspace(0, 10, 10 * fs)
ecg = 0.5 * np.sin(2 * np.pi * 1 * t) + 0.1 * np.random.normal(0, 0.1, len(t))

# Apply wavelet denoising
coeffs = pywt.wavedec(ecg, 'db4', level=4)
threshold = 0.1 * np.std(coeffs[-1])
coeffs = [pywt.threshold(c, threshold, mode='soft') for c in coeffs]
ecg_denoised = pywt.waverec(coeffs, 'db4')

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], ecg[:1000], label='Noisy ECG')
plt.plot(t[:1000], ecg_denoised[:1000], label='Wavelet Denoised ECG')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('ECG Wavelet Denoising')
plt.legend()
plt.grid()
plt.show()
