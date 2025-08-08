import neurokit2 as nk
import matplotlib.pyplot as plt

# Simulate ECG signal
fs = 1000
ecg = nk.ecg_simulate(duration=10, sampling_rate=fs, heart_rate=70)

# Detect P, QRS, T waves
ecg_cleaned = nk.ecg_clean(ecg, sampling_rate=fs)
signals, waves = nk.ecg_delineate(ecg_cleaned, sampling_rate=fs)

# Plot ECG with P, QRS, T annotations
plt.figure(figsize=(10, 4))
plt.plot(ecg, label='ECG Signal')
plt.scatter(waves['ECG_P_Peaks'], ecg[waves['ECG_P_Peaks']], color='green', label='P Peaks')
plt.scatter(waves['ECG_R_Peaks'], ecg[waves['ECG_R_Peaks']], color='red', label='R Peaks')
plt.scatter(waves['ECG_T_Peaks'], ecg[waves['ECG_T_Peaks']], color='blue', label='T Peaks')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.title('ECG PQRST Segmentation')
plt.legend()
plt.grid()
plt.show()
