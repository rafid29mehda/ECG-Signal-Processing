import neurokit2 as nk
import matplotlib.pyplot as plt
import numpy as np

# Simulate ECG signal
fs = 1000
ecg = nk.ecg_simulate(duration=10, sampling_rate=fs, heart_rate=70)

# Compute Short-Time Fourier Transform (STFT)
f, t, Zxx = nk.signal_timefrequency(ecg, sampling_rate=fs, method='stft', window_size=256)

# Plot time-frequency representation
plt.figure(figsize=(10, 4))
plt.pcolormesh(t, f, np.abs(Zxx), shading='auto')
plt.colorbar(label='Amplitude')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.title('ECG Time-Frequency Analysis (STFT)')
plt.ylim(0, 50)  # Focus on relevant frequency range
plt.show()
