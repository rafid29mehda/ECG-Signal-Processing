import neurokit2 as nk
import numpy as np
import heartpy as hp
import matplotlib.pyplot as plt

# Simulate ECG signal
fs = 1000
ecg = nk.ecg_simulate(duration=10, sampling_rate=fs, heart_rate=70)

# Segment beats and extract features
ecg_cleaned = nk.ecg_clean(ecg, sampling_rate=fs)
working_data, measures = hp.process(ecg_cleaned, sample_rate=fs)

# Plot a single beat
beat = working_data['peaklist'][0]
beat_samples = ecg_cleaned[beat-50:beat+50]
plt.figure(figsize=(10, 4))
plt.plot(beat_samples, label='Single ECG Beat')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.title('ECG Beat Segmentation and Analysis')
plt.legend()
plt.grid()
plt.show()

# Print basic beat features
print(f"Heart Rate: {measures['bpm']:.2f} BPM")
print(f"IBI: {measures['ibi']:.2f} ms")
