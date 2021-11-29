import cv2
import numpy

#multiple image operations:
image1 = cv2.imread('nature.jpg',1)
image2 = cv2.imread('nature1.jpg',1)

image3 = image1 + image2
image3 = cv2.bitwise_and(image2,image1)

cv2.imshow('image3',image3)
cv2.waitKey(0)
image4 = image1 - image2
image4 = cv2.bitwise_and(image2,image1)

cv2.imshow('image4',image3)
cv2.waitKey(0)