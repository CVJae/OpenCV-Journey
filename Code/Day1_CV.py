import cv2 as cv 

# Reading Images.

img = cv.imread('Photos/snowcat.jpg')

# cv.imshow('snowcat', img)

# cv.waitKey(0)

# ----------------------------

# Inspecting Image

print(img.shape)
print(img[0, 0])


# GreyScale image.

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("gray image", gray)


cap = cv.VideoCapture('Outside.mov')

for i in range(10):
    ret, frame = cap.read()
    if ret:
        cv.imwrite(f"frame_{i}.jpg", frame)
cap.release()