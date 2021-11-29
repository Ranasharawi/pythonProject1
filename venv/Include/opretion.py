import cv2

img = cv2.imread('lady.jpg', 0)
print(img)

#rows ,cols = img.shape

rows = img.shape[0]
cols = img.shape[1]

