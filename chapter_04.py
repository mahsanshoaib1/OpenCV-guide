                                        # converting into black and white
# importing libraries
import cv2 as cv

# importing an image
img = cv.imread("resources/img.jpeg")

# resize
img = cv.resize(img, (600,750))

# conversions
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary)= cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# display the image
cv.imshow("pehli image" , img)
cv.imshow("gray image" , gray)
cv.imshow("black", binary)

# time for delay
cv.waitKey(0)