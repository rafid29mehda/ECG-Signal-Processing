import neurokit2 as nk
import numpy as np
import matplotlib.pyplot as plt

# Simulate ECG signal
fs = 1000
ecg = nk.ecg_simulate(duration=10, sampling_rate=fs, heart_rate=70)

# Detect R-peaks and compute RR intervals
ecg_cleaned = nk.ecg_clean(ecg, sampling_rate=fs)
rpeaks = nk.ecg_peaks(ecg_cleaned, sampling_rate=fs)[1]['ECG_R_Peaks']
rr_intervals = np.diff(rpeaks) / fs * 1000  # In ms

# Compute sample entropy
entropy = nk.entropy_sample(rr_intervals, dimension=2, tolerance=0.2 * np.std(rr_intervals))

# Plot RR intervals and print entropy
plt.figure(figsize=(10, 4))
plt.plot(rr_intervals, label='RR Intervals')
plt.xlabel('Beat Number')
plt.ylabel('RR Interval (ms)')
plt.title(f'ECG Entropy Analysis (Sample Entropy: {entropy:.2f})')
plt.legend()
plt.grid()
plt.show()
