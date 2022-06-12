import cv2
import numpy 


img = cv2.imread("img/image.jpeg")

# def rotate(img, angle):
#     h,w = img.shape[:2]
#     point = (w//2,h//2)

#     mat = cv2.getRotationMatrix2D(point,angle,1)
#     return cv2.warpAffine(img,mat, (w,h))

# img = cv2.flip(img, 1)
# img = rotate(img,180)

newImg = numpy.zeros(img.shape, dtype='uint8')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.GaussianBlur(img,(5,5), 0)

img = cv2.Canny(img, 100, 140)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(newImg, con, -1, (95,123,12),thickness=2)



#print(con)

cv2.imshow('1', newImg)

cv2.waitKey(0)