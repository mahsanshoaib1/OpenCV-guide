                                        # resize the image
# importing libraries
import cv2 as cv

# importing an image
img = cv.imread("resources/img.jpeg")

# resizing the image
img1 = cv.resize(img, (600, 740))

# display the image
cv.imshow("pehli image", img)
cv.imshow("resize image", img1)


# time for being show
cv.waitKey(0)



