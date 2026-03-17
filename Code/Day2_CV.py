import cv2 as cv

# Load image
img = cv.imread('Photos/snowcat.jpg')

# Show original
cv.imshow("Original", img)

# Resize image
resized = cv.resize(img, (500, 500))
cv.imshow("Resized", resized)

# Crop image
cropped = img[50:400, 50:400]
cv.imshow("Cropped", cropped)

# Flip image
flipped = cv.flip(img, 1)
cv.imshow("Flipped", flipped)

cv.waitKey(0)
cv.destroyAllWindows()

