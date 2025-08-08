import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Simulate ECG signal
fs = 1000  # Sampling frequency (Hz)
t = np.linspace(0, 10, 10 * fs)  # 10 seconds
ecg = 0.5 * np.sin(2 * np.pi * 1 * t) + 0.2 * np.random.normal(0, 0.1, len(t))  # Simulated ECG with noise

# Apply bandpass filter (0.5-40 Hz to remove baseline wander and high-frequency noise)
b, a = signal.butter(4, [0.5, 40], btype='bandpass', fs=fs)
ecg_filtered = signal.filtfilt(b, a, ecg)

# Plot raw and filtered ECG
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], ecg[:1000], label='Raw ECG')
plt.plot(t[:1000], ecg_filtered[:1000], label='Filtered ECG')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('ECG Preprocessing: Bandpass Filtering')
plt.legend()
plt.grid()
plt.show()
