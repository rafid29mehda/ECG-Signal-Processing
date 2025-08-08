import neurokit2 as nk
import numpy as np
import matplotlib.pyplot as plt

# Simulate ECG signal
fs = 1000
ecg = nk.ecg_simulate(duration=10, sampling_rate=fs, heart_rate=70)

# Detect QRS complexes
ecg_cleaned = nk.ecg_clean(ecg, sampling_rate=fs)
signals, waves = nk.ecg_delineate(ecg_cleaned, sampling_rate=fs)
qrs_starts = waves['ECG_Q_Peaks']
qrs_ends = waves['ECG_S_Peaks']

# Calculate QRS duration
qrs_durations = (qrs_ends - qrs_starts) / fs * 1000  # In ms
print(f"Average QRS Duration: {np.nanmean(qrs_durations):.2f} ms")

# Plot
plt.figure(figsize=(10, 4))
plt.plot(ecg, label='ECG Signal')
plt.scatter(qrs_starts, ecg[qrs_starts], color='green', label='Q Peaks')
plt.scatter(qrs_ends, ecg[qrs_ends], color='blue', label='S Peaks')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.title('ECG QRS Duration Analysis')
plt.legend()
plt.grid()
plt.show()
