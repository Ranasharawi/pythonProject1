import cv2
import numpy

img = cv2.imread('cars.jpg',1)
cv2.imshow('original.jpg',img)
cv2.waitKey(0)

blue = img[:,:,0]
blueRows, blueCols = blue.shape
'''
cv2.imshow('blue.jpg',blue)
cv2.waitKey(0)
'''

red = img[:,:,2]
redRows , redCols = red.shape
'''
cv2.imshow('red.jpg',red)
cv2.waitKey(0)
'''
green = img[:,:,1]
greenRows , greenCols = green.shape
'''
cv2.imshow('green.jpg',green)
cv2.waitKey(0)
'''

#Changing the image lighting color:
def blueAdd():
    for i in range(blueRows):
        for j in range(blueCols):
            pixel = blue[i,j]
            newPixel = pixel + 128
            if newPixel > 255:
                blue[i,j] = 255
            elif newPixel < 0:
                blue[i,j] = 0
            else:
                blue[i,j] = newPixel

blueAdd()
cv2.imshow('moreBlue',img)
cv2.waitKey(0)

def redAdd():
    for i in range(redRows):
        for j in range(redCols):
            pixel = red[i,j]
            newPixel = pixel + 128
            if newPixel > 255:
                red[i,j] = 255
            elif newPixel < 0:
                red[i,j] = 0
            else:
                red[i,j] = newPixel

redAdd()
cv2.imshow('moreRed',img)
cv2.waitKey(0)

def greenAdd():
    for i in range(greenRows):
        for j in range(greenCols):
            pixel = green[i,j]
            newPixel = pixel + 128
            if newPixel>255:
                green[i,j]=255
            elif newPixel<0:
                green[i,j]=0
            else:
                green[i,j]=newPixel

greenAdd()
cv2.imshow('moreGreen',img)
cv2.waitKey(0)

########################################################################################

#swapping image channels:
img[:,:,0]=red

cv2.imshow('swappingBlueWithRed',img)
cv2.waitKey(0)

########################################################################################

#eliminating colors channels:
img[:,:,2] = numpy.zeros([img.shape[0], img.shape[1]])

cv2.imshow('delRed',img)
cv2.waitKey(0)

########################################################################################