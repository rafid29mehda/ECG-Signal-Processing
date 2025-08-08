import neurokit2 as nk
import numpy as np
import matplotlib.pyplot as plt

# Simulate ECG signal
fs = 1000
ecg = nk.ecg_simulate(duration=10, sampling_rate=fs, heart_rate=70)

# Detect P-waves
ecg_cleaned = nk.ecg_clean(ecg, sampling_rate=fs)
signals, waves = nk.ecg_delineate(ecg_cleaned, sampling_rate=fs)
p_peaks = waves['ECG_P_Peaks']

# Calculate P-wave amplitude
p_amplitudes = ecg[p_peaks]
print(f"Average P-wave Amplitude: {np.nanmean(p_amplitudes):.2f}")

# Plot
plt.figure(figsize=(10, 4))
plt.plot(ecg, label='ECG Signal')
plt.scatter(p_peaks, ecg[p_peaks], color='green', label='P Peaks')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.title('ECG P-Wave Analysis')
plt.legend()
plt.grid()
plt.show()
