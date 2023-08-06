                                            # joining two images

'''
    Note: You can only stack two images of same shape i.e same height, width, color channnel
'''

import cv2 as cv
import numpy as np

# hstack( example)
a1 = np.arange(1,6, dtype=int,)
a2 = np.arange(6,11, dtype=int,)

a3 = np.hstack((a1,a2))
# print(a3)

# reading image
img = cv.imread("resources/img.jpeg")
img = cv.resize(img, (400,500))

# joining horizontly
h_img = np.hstack((img, img))   # join two arrays horizontly

# joining vertically
v_img = np.vstack((img, img))   # join two arrays horizontly

# inverting image
i_img = np.invert(img)

# displaying the image
cv.imshow("himg", h_img)
cv.imshow("vimg", v_img)
cv.imshow("iimg", i_img)
cv.waitKey(10000)
cv.destroyAllWindows()



