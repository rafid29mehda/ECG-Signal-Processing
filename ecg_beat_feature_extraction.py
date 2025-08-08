import heartpy as hp
import matplotlib.pyplot as plt

# Simulate ECG signal
fs = 1000
ecg = hp.get_data('example_data.csv') if hp.get_data('example_data.csv') is not None else hp.simulate_ecg(fs=fs, duration=10)

# Process ECG and extract features
working_data, measures = hp.process(ecg, sample_rate=fs)

# Plot with detected peaks
plt.figure(figsize=(10, 4))
plt.plot(ecg, label='ECG Signal')
plt.scatter(working_data['peaklist'], ecg[working_data['peaklist']], color='red', label='R-Peaks')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.title('ECG Beat Feature Extraction')
plt.legend()
plt.grid()
plt.show()

# Print features
print(f"BPM: {measures['bpm']:.2f}")
print(f"SDNN: {measures['sdnn']:.2f} ms")
