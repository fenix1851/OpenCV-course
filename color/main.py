import cv2
import numpy

img = cv2.imread("./src/img/image.jpeg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img)
 
img = cv2.merge([b,g,r])

cv2.imshow("Res", img)
cv2.waitKey(0)
