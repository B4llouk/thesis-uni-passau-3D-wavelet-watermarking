import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import zoom
import pywt


def randomWatermark(): 
    return np.random.randint(0, 250, size=(104, 116, 116))

def reshapeWm(watermark, watermark_shape):
    watermark = zoom(watermark, (watermark_shape[1] / watermark.shape[0], watermark_shape[2] / watermark.shape[1]), order=0)
    watermark= np.tile(watermark, (watermark_shape[0], 1, 1)) 
    return watermark


def retrieveWm(original_data, watermarked_coeffs, wavelet, alpha):
    # Perform 3D DWT on the original data
    coefficients = pywt.dwtn(original_data, wavelet, mode='symmetric', axes=None)
    # Extract the approximation coefficients from the DWT
    approx_coeffs = coefficients['aaa']
    
    # Retrieve the watermarked approximation coefficients
    watermarked_approx_coeffs = watermarked_coeffs['aaa']
    
    # Calculate the difference between watermarked and original approximation coefficients
    diff_coeffs = watermarked_approx_coeffs - approx_coeffs
    
    
    # Scale the resized difference coefficients back to the watermark scale
    retrieved_watermark = diff_coeffs  / alpha
    
    return retrieved_watermark

def recreate2Dwm(watermark3D):
    return np.mean(watermark3D, axis=0)



