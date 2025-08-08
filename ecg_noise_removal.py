import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Simulate ECG with noise
fs = 1000
t = np.linspace(0, 10, 10 * fs)
ecg = 0.5 * np.sin(2 * np.pi * 1 * t) + 0.1 * np.sin(2 * np.pi * 50 * t) + 0.1 * np.random.normal(0, 0.1, len(t))

# Apply notch filter to remove 50 Hz powerline noise
b, a = signal.iirnotch(50, 30, fs=fs)
ecg_notch = signal.filtfilt(b, a, ecg)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], ecg[:1000], label='Noisy ECG')
plt.plot(t[:1000], ecg_notch[:1000], label='Notch Filtered ECG')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('ECG Noise Removal (50 Hz Notch Filter)')
plt.legend()
plt.grid()
plt.show()
