# importing libraries
import cv2 as cv

#importing an image
img = cv.imread("resources/img.jpeg", 1)  # 1 is for colored image

img1 = cv.imread("resources/img.jpeg", 0) # 0 is for gray scalled image

img2 = cv.imread("resources/img.jpeg", -1)

# to test if image is uploaded
print(img) # if none then pic is not read

# display the image
cv.imshow("pehli image", img)

cv.imshow("dosri image", img1)

cv.imshow("teesri image", img2)


# time for being show. time in miliseconds 
# cv.waitKey(0)  # 0 = infinity

cv.waitKey(5000)  # 5 seconds


# there are two kinds of images, colored images = RGB, and gray scalled images