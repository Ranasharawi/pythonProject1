import cv2
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('flower', img)
key = cv2.waitKey(0)
cv2.imwrite('rana.jpg',img)
if (key ==ord('a')):
    cv2.imwrite ('dd.jpg',img)
elif (key==ord('s')):
    plt.imshow(img,cmap='gist_ncar')
    plt.show()
z