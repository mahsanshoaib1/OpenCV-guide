                                            # functions for images

# importing library
import cv2 as cv
import numpy as np

# reading the image
img = cv.imread("resources/img.jpeg")
img = cv.resize(img,(450,600))

# resizing the image
resize_img = cv.resize(img,(450,600))

# gray colored image
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blured image
blur_img = cv.GaussianBlur(img,(7,7), 10)

# only edges with be highlited
edge_img = cv.Canny(img, 60,60)
dilated_img = cv.dilate(edge_img,(20,20), iterations=1)
ero_image = cv.erode(dilated_img, (43,43))

# cropping an image, we use numpy to crop the image not open cv
print("the size of our image is: ", np.shape(img))
croped_img = resize_img[30:, 100:350]

# wirte/displayng the image
cv.imshow("image", img)
cv.imshow("reimage", resize_img)
cv.imshow("gray image", gray_img)
cv.imshow("blur_img", blur_img)
cv.imshow("edge_img", edge_img)
cv.imshow("dilate_img", dilated_img)
cv.imshow("ero_img", ero_image)
cv.imshow("cropped image", croped_img)


cv.waitKey(0)
cv.destroyAllWindows()