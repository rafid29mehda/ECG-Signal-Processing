import neurokit2 as nk
import matplotlib.pyplot as plt

# Simulate ECG with noise
fs = 1000
ecg = nk.ecg_simulate(duration=10, sampling_rate=fs, heart_rate=70, noise=0.2)

# Assess signal quality
ecg_cleaned = nk.ecg_clean(ecg, sampling_rate=fs)
quality = nk.ecg_quality(ecg_cleaned, sampling_rate=fs)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(ecg, label=f'ECG Signal (Quality: {quality})')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.title('ECG Signal Quality Assessment')
plt.legend()
plt.grid()
plt.show()
