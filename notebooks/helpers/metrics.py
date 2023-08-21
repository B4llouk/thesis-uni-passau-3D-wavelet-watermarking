import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr

def calculate_psnr_skimage(original, distorted):
    # Ensure the inputs are numpy arrays
    original = np.array(original)
    distorted = np.array(distorted)

    # Calculate the peak signal value based on the max and min values of the original array
    peak_signal_value = original.max() - original.min()

    # Calculate PSNR using skimage.metrics.peak_signal_noise_ratio
    psnr_value = psnr(original, distorted, data_range=peak_signal_value)
    return psnr_value