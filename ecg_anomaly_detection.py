import neurokit2 as nk
import numpy as np
import matplotlib.pyplot as plt

# Simulate ECG with anomaly
fs = 1000
ecg = nk.ecg_simulate(duration=10, sampling_rate=fs, heart_rate=70)
ecg[4000:4100] += 0.5  # Add artificial anomaly

# Detect R-peaks and compute RR intervals
ecg_cleaned = nk.ecg_clean(ecg, sampling_rate=fs)
rpeaks = nk.ecg_peaks(ecg_cleaned, sampling_rate=fs)[1]['ECG_R_Peaks']
rr_intervals = np.diff(rpeaks) / fs * 1000  # RR intervals in ms

# Detect anomalies (e.g., RR intervals deviating > 2 std)
mean_rr = np.mean(rr_intervals)
std_rr = np.std(rr_intervals)
anomalies = np.where((rr_intervals < mean_rr - 2*std_rr) | (rr_intervals > mean_rr + 2*std_rr))[0]

# Plot
plt.figure(figsize=(10, 4))
plt.plot(rr_intervals, label='RR Intervals')
plt.scatter(anomalies, rr_intervals[anomalies], color='red', label='Anomalies')
plt.xlabel('Beat Number')
plt.ylabel('RR Interval (ms)')
plt.title('ECG Anomaly Detection')
plt.legend()
plt.grid()
plt.show()
