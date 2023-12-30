import cv2
import numpy as np

def rgb_to_xyz(rgb):
    # Transformasi matriks untuk RGB ke XYZ
    m = np.array([[0.4124564, 0.3575761, 0.1804375],
                  [0.2126729, 0.7151522, 0.0721750],
                  [0.0193339, 0.1191920, 0.9503041]])
    
    xyz = np.dot(rgb, m.T)
    return xyz

# Load citra RGB
image_rgb = cv2.imread('1.png')

# Normalisasi nilai piksel ke rentang [0, 1]
image_rgb = image_rgb / 255.0

# Transformasi RGB ke XYZ
image_xyz = rgb_to_xyz(image_rgb)

# Tampilkan citra hasil
cv2.imshow('RGB Image', image_rgb)
cv2.imshow('XYZ Image', image_xyz)
cv2.waitKey(0)
cv2.destroyAllWindows()
