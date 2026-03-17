import cv2 as cv

# Load image
img = cv.imread('Photos/snowcat.jpg')

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Blur image
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

# Edge detection
edges = cv.Canny(blur, 50, 150)

cv.imshow("Original", img)
cv.imshow("Edges", edges)

cv.waitKey(0)
cv.destroyAllWindows()