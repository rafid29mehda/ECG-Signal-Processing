import neurokit2 as nk
import matplotlib.pyplot as plt

# Simulate ECG signal
fs = 1000
ecg = nk.ecg_simulate(duration=10, sampling_rate=fs, heart_rate=70)

# Detect R-peaks using NeuroKit2
ecg_cleaned = nk.ecg_clean(ecg, sampling_rate=fs)
rpeaks = nk.ecg_peaks(ecg_cleaned, sampling_rate=fs)[1]['ECG_R_Peaks']

# Plot ECG with detected R-peaks
plt.figure(figsize=(10, 4))
plt.plot(ecg, label='ECG Signal')
plt.scatter(rpeaks, ecg[rpeaks], color='red', label='R-Peaks')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.title('ECG R-Peak Detection')
plt.legend()
plt.grid()
plt.show()
