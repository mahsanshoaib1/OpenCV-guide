                                        # converting into gray shadows
# importing libraries
import cv2 as cv

# importing an image
img = cv.imread("resources/img.jpeg")

# conversion
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# display the image
cv.imshow("pehli image", img)
cv.imshow("resize image", gray_img)


# time for delay
cv.waitKey(0)