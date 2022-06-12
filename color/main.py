import cv2
import numpy

img = cv2.imread("./src/img/image.jpeg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Res", img)
cv2.waitKey(0)
