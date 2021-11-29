import cv2

img = cv2.imread('flower.jpg', 0)

#rows ,cols = img.shape

rows = img.shape[0]
cols = img.shape[1]

print('rows=', rows)
print('cols=', cols)


def add():
    for i in range(rows):
        for j in range(cols):
            pixel = img[i, j]
            newPixel = pixel+128

            if newPixel > 255:
                img[i, j] = 255
            elif newPixel < 0:
                img[i, j] = 0
            else:
                img[i, j] = newPixel

add()
cv2.imshow('addition', img)
cv2.waitKey(0)
cv2.imwrite('addition.jpg', img)

def subtraction():
    for i in range(rows):
        for j in range(cols):
            pixel = img[i, j]
            newPixel = pixel-128
            if newPixel<0:
                img[i, j]=0
            else:
                img[i, j]=newPixel
subtraction()
cv2.imshow('subtraction',img)
cv2.waitKey(0)
cv2.imwrite('subtraction.jpg',img)

def mul():
    for i in range(rows):
        for j in range(cols):
            pixel=img[i,j]
            newPixel=pixel*2
            if newPixel<0:
                img[i,j]=0
            else:
                img[i,j]=newPixel
mul()
cv2.imshow('multiplication',img)
cv2.waitKey(0)
cv2.imwrite('multiplication.jpg',img)

def complemetary():
    for i in range(rows):
        for j in range(cols):
            pixel=img[i,j]
            newPixel=255 - pixel
            if newPixel<0:
                img[i,j]=0
            else:
                img[i,j]=newPixel
complemetary()
cv2.imshow('comolemenraty',img)
cv2.waitKey(0)
cv2.imwrite('comolemenraty.jpg',img)