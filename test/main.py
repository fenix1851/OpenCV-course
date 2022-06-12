from datetime import date
import cv2
import numpy

# img = cv2.imread('img/image.jpeg')

# img = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2))

# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# # img = cv2.GaussianBlur(img, (15, 15), 0)

# cv2.imshow('kitten',img)


# cv2.waitKey(0)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = cv2.rotate(img, cv2.ROTATE_180)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.Canny(img, 15, 15)
    kernel = numpy.ones((3,3), numpy.uint8)
    img = cv2.dilate(img, kernel, iterations=1)

    img = cv2.erode(img, kernel, iterations=1)

    cv2.imshow('ok', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break