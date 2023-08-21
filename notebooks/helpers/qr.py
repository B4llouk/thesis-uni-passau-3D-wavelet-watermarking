import qrcode
from PIL import Image
import numpy as np

def createQr(path):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(path)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")
    return qr_image 

def qrToArray(qrImagePath):
    qrImage = Image.open(qrImagePath)
    qrArray = np.array(qrImage)
    watermark= qrArray.astype(np.uint8) * 255
    print(watermark)
    return watermark

def qrToWatermark(qrArray, newSize):
    #First step is to reshape the watermark 
    # Resize the QR code array using scipy.ndimage.zoom()
    resized_qr_array = zoom(qrArray, (newSize[1] / qr_array.shape[0], newSize[2] / qr_array.shape[1]), order=0)

    # stack the qr x times on top of itself in order to create redundancy and make it a 3D array 
    watermark = np.tile(resized_qr_array, (newSize[0], 1, 1))

    return watermark  