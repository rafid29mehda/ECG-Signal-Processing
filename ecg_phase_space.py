import neurokit2 as nk
import numpy as np
import matplotlib.pyplot as plt

# Simulate ECG signal
fs = 1000
ecg = nk.ecg_simulate(duration=10, sampling_rate=fs, heart_rate=70)
ecg_cleaned = nk.ecg_clean(ecg, sampling_rate=fs)

# Create phase space (time-delay embedding)
delay = 10  # Time delay in samples
ecg_delayed = ecg_cleaned[delay:]
ecg_original = ecg_cleaned[:-delay]

# Plot 2D phase space
plt.figure(figsize=(8, 8))
plt.plot(ecg_original, ecg_delayed, label='Phase Space Trajectory')
plt.xlabel('ECG(t)')
plt.ylabel(f'ECG(t + {delay/fs:.2f}s)')
plt.title('ECG Phase Space Analysis')
plt.legend()
plt.grid()
plt.show()
