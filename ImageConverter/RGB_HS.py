import cv2
import numpy as np

def rgb_to_hs(rgb):
    # Konversi RGB ke HSV
    hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
    return hsv

# Load citra RGB
image_rgb = cv2.imread('1.png')

# Transformasi RGB ke HS
image_hs = rgb_to_hs(image_rgb)

# Tampilkan citra hasil
cv2.imshow('RGB Image', image_rgb)
cv2.imshow('HS Image', image_hs)
cv2.waitKey(0)
cv2.destroyAllWindows()
