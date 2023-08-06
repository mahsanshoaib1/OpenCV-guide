                                # how to draw an image and lines and shapes in an image
#importing libraries
import cv2 as cv
import numpy as np

# making an image
img = np.zeros((600,600)) # 0 is for black
img1 = np.ones((600,600)) # 1 is for white

# adding color to the canvas
colored_img = np.zeros((600,600, 3), np.uint8) # adding new channel
colored_img[ : ] = 0,70,205   # full pic color
# colored_img[30 : 300, 100:250] = 0,70,205  # croped

#adding line to the image
cv.line(colored_img, (0, 0) , (600, 600), (170,100, 115), 4)
cv.line(colored_img, (300, 0) , (300, 600), (120,45, 127), 3)
# cv.line(colored_img, (horizontal_position, verticle_position) , (angle, length), (Red, green, brown), 
#    thickness)

# rectangle in the image
cv.rectangle(colored_img, (500,300), (200,200), (255,255,255), cv.FILLED) # filled
cv.rectangle(colored_img, (500,500), (550,150), (100,200,155), 2) # draw
# (300,100) is the (left line-top line) corner and (200,150) is the(right line-bottom line) corner.

# cirlce in the image
cv.circle(colored_img, (400,400), 100, (200,200,240), 3)

# adding text to the image
cv.putText(colored_img, "hi, how are you doing buddy", (30, 340), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0,252,0),2)


#displaying the image
cv.imshow("bimg", img)
cv.imshow("wimg", img1)
cv.imshow("cimg", colored_img)


cv.waitKey(0)
cv.destroyAllWindows()