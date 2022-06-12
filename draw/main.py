from ast import While
from random import randrange
import cv2
import numpy 

img = numpy.zeros((300,500,3), dtype ="uint8")

color = 243,54,76
color1 = 23, 54, 129


# img[100:150, 200:250] = B, G, R
# cv2.rectangle(img, (40,40), (150,1000), color, thickness =3)
cv2.putText(img, 'Hello world', (100,150), cv2.FONT_HERSHEY_COMPLEX, 1, color,1)
# while True:
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
cv2.imshow('img', img)

cv2.waitKey(0)
