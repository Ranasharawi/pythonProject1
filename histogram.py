from matplotlib import pyplot as plt
import cv2

#Histogram with gray scale image:
img = cv2.imread('car (2).jpg', 0)

new = img.ravel()
plt.hist(new,10,[0,100])

plt.show()