import numpy as np
import cv2

print("MUZAMMIL EP1850097")

# load spritesheet
img = cv2.imread('spritesheet.png',1)

minHeight = 0
minWidth = 0

# heigth distance of every sprite character
heightDistance = 200

# width distance of every sprite character
widthDistance = 169


              # height width
# sprite1 = img[0:200, 0:180]


# First Row
for x in range(1,6):

    maxHeight = minHeight+heightDistance
    maxWidth = minWidth+widthDistance

    # From img take pixel of this height & width
    sprite1 = img[minHeight:maxHeight, minWidth:maxWidth]
    # print("Sprite",minHeight,maxHeight,minWidth,maxWidth)

    cv2.imwrite("sprite"+str(x)+".png", sprite1)
    minWidth = minWidth + widthDistance


# Reset width & height for second row (out of loop 1)
minHeight = minHeight + heightDistance
minWidth = 0

# First Second Row
for x in range(6,11):

    maxHeight = minHeight+heightDistance
    maxWidth = minWidth+widthDistance

    sprite1 = img[minHeight:maxHeight, minWidth:maxWidth]

    # print("SpriteR",minHeight,maxHeight,minWidth,maxWidth)
    cv2.imwrite("sprite"+str(x)+".png", sprite1)

    minWidth = minWidth + widthDistance


# Output window for spritesheet
cv2.namedWindow("output", cv2.WINDOW_NORMAL)       
imS = cv2.resize(img, (960, 540))                   

cv2.imshow('image',imS)
cv2.waitKey(0)
cv2.destroyAllWindows()