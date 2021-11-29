from matplotlib import pyplot as plt
import cv2

img= cv2.imread('flower.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap='gist_ncar')
plt.xticks([])
plt.yticks([])
plt.show()
