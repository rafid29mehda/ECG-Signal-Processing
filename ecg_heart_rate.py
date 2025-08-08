import neurokit2 as nk
import numpy as np

# Simulate ECG signal
fs = 1000
ecg = nk.ecg_simulate(duration=10, sampling_rate=fs, heart_rate=70)

# Detect R-peaks and compute heart rate
ecg_cleaned = nk.ecg_clean(ecg, sampling_rate=fs)
rpeaks = nk.ecg_peaks(ecg_cleaned, sampling_rate=fs)[1]['ECG_R_Peaks']
rr_intervals = np.diff(rpeaks) / fs  # RR intervals in seconds
heart_rate = 60 / rr_intervals  # Heart rate in BPM

# Print average heart rate
print(f"Average Heart Rate: {np.mean(heart_rate):.2f} BPM")

# Plot heart rate over time
plt.figure(figsize=(10, 4))
plt.plot(rpeaks[1:] / fs, heart_rate, label='Heart Rate')
plt.xlabel('Time (s)')
plt.ylabel('Heart Rate (BPM)')
plt.title('Heart Rate Calculation from ECG')
plt.legend()
plt.grid()
plt.show()
