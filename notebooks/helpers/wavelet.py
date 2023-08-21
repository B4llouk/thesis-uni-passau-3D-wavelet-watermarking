import numpy as np
import pywt
import helpers.wm

# add the watermark to coefficients
def embedWatermarkAddition(original_data, watermark, wavelet, alpha):
    # Perform 3D DWT on the original data
    coefficients = pywt.dwtn(original_data, wavelet, mode='symmetric', axes=None)

    # Extract the approximation coefficients from the DWT
    #brings out half
    approx_coeffs = coefficients['aaa']

    #resize watermark 
    resizedWatermark= helpers.wm.reshapeWm(watermark, approx_coeffs.shape)
    # Scale the watermark by alpha
    scaledWm = np.multiply(resizedWatermark, alpha)

    # Embed the watermark by adding it to the approximation coefficients
    watermarked_coeffs = approx_coeffs + scaledWm 

    # Create a new dictionary with the watermarked coefficients
    watermarked_coeffs_dict = dict(coefficients)
    watermarked_coeffs_dict['aaa'] = watermarked_coeffs

    return watermarked_coeffs_dict


# Function to reconstruct the watermarked volume using IDWT
def reconstructWmVolume(watermarked_coeffs, wavelet):
    # Perform inverse 3D DWT to reconstruct the watermarked volume
    watermarked_data = pywt.idwtn(watermarked_coeffs, wavelet, mode='symmetric', axes=None)
    return watermarked_data


def wavelist():
    return pywt.wavelist(kind='discrete')
