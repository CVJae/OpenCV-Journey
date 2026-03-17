import cv2 as cv
import numpy as np

# Load image
img = cv.imread('Photos/snowcat.jpg')

# Convert image to HSV color space
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Define color range (detect light/white areas)
lower = np.array([0, 0, 200])
upper = np.array([180, 40, 255])

# Create mask
mask = cv.inRange(hsv, lower, upper)

# Apply mask
result = cv.bitwise_and(img, img, mask=mask)

cv.imshow('Original Image', img)
cv.imshow('Mask', mask)
cv.imshow('Detected Color', result)

cv.waitKey(0)
cv.destroyAllWindows()