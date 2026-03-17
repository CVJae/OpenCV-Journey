import cv2 as cv

# Load image
img = cv.imread('Photos/snowcat.jpg')

# Convert image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply blur to reduce noise
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

# Detect edges
canny = cv.Canny(blur, 50, 150)

# Find contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contours found.')

# Draw contours on image
blank = img.copy()
cv.drawContours(blank, contours, -1, (0, 255, 0), 2)

cv.imshow('Original Image', img)
cv.imshow('Edges', canny)
cv.imshow('Contours', blank)

cv.waitKey(0)
cv.destroyAllWindows()