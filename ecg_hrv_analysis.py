import neurokit2 as nk
import matplotlib.pyplot as plt

# Simulate ECG signal
fs = 1000
ecg = nk.ecg_simulate(duration=60, sampling_rate=fs, heart_rate=70)

# Compute HRV metrics
ecg_cleaned = nk.ecg_clean(ecg, sampling_rate=fs)
rpeaks = nk.ecg_peaks(ecg_cleaned, sampling_rate=fs)[1]['ECG_R_Peaks']
hrv_metrics = nk.hrv_time(rpeaks, sampling_rate=fs)

# Print key HRV metrics
print("HRV Metrics:")
print(f"SDNN: {hrv_metrics['HRV_SDNN'][0]:.2f} ms")
print(f"RMSSD: {hrv_metrics['HRV_RMSSD'][0]:.2f} ms")

# Plot RR intervals
rr_intervals = np.diff(rpeaks) / fs * 1000  # Convert to ms
plt.figure(figsize=(10, 4))
plt.plot(rr_intervals, label='RR Intervals')
plt.xlabel('Beat Number')
plt.ylabel('RR Interval (ms)')
plt.title('Heart Rate Variability (HRV) Analysis')
plt.legend()
plt.grid()
plt.show()
