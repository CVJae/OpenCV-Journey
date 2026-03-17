import cv2 as cv

# Load video
cap = cv.VideoCapture('Videos/Outside.mov')

while True:
    ret, frame = cap.read()

    if not ret:
        print("Video ended or failed to load.")
        break

    # Convert frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("Original Video", frame)
    cv.imshow("Grayscale Video", gray)

    # Press D to exit
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()