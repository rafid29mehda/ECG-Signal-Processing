import numpy as np
import scipy.fftpack as fftpack
import matplotlib.pyplot as plt

# Simulate ECG signal
fs = 1000
t = np.linspace(0, 10, 10 * fs)
ecg = 0.5 * np.sin(2 * np.pi * 1 * t) + 0.1 * np.random.normal(0, 0.1, len(t))

# Apply Discrete Cosine Transform (DCT)
dct_coeffs = fftpack.dct(ecg, norm='ortho')
# Keep only top 10% of coefficients for compression
threshold = int(0.1 * len(dct_coeffs))
dct_coeffs[threshold:] = 0
# Reconstruct signal using inverse DCT
ecg_reconstructed = fftpack.idct(dct_coeffs, norm='ortho')

# Calculate compression ratio and reconstruction error
compression_ratio = 100 * (1 - threshold / len(dct_coeffs))
mse = np.mean((ecg - ecg_reconstructed) ** 2)
print(f"Compression Ratio: {compression_ratio:.2f}%")
print(f"Mean Squared Error: {mse:.4f}")

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], ecg[:1000], label='Original ECG')
plt.plot(t[:1000], ecg_reconstructed[:1000], label='Reconstructed ECG')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('ECG Signal Compression using DCT')
plt.legend()
plt.grid()
plt.show()
