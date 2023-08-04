                                        # saving the image
# importing libraries
import cv2 as cv

# importing an image
img = cv.imread("resources/img.jpeg")

# resize
img = cv.resize(img, (600,750))

# conversions
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary)= cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

binary = cv.resize(binary, (800, 1000))

# display the image
'''
cv.imshow("pehli image" , img)
cv.imshow("gray image" , gray)
cv.imshow("black", binary)
'''

# save. write the image
cv.imwrite("resources/gray.jpg", gray)
cv.imwrite("resources/black.jpeg", binary)

# time for delay
cv.waitKey(0)