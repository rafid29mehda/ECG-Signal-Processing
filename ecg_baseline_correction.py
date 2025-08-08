import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Simulate ECG with baseline wander
fs = 1000
t = np.linspace(0, 10, 10 * fs)
ecg = 0.5 * np.sin(2 * np.pi * 1 * t) + 0.2 * np.sin(2 * np.pi * 0.05 * t)  # Baseline wander

# Apply high-pass filter to remove baseline wander
b, a = signal.butter(4, 0.5, btype='highpass', fs=fs)
ecg_corrected = signal.filtfilt(b, a, ecg)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], ecg[:1000], label='ECG with Baseline Wander')
plt.plot(t[:1000], ecg_corrected[:1000], label='Baseline Corrected ECG')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('ECG Baseline Correction')
plt.legend()
plt.grid()
plt.show()
