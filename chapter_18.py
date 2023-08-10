import cv2 as cv
import numpy as np


# def click(event, x, y, params, flags):
#     if event == cv.EVENT_FLAG_LBUTTON:
#         print(x, ", " , y)
#         font = cv.FONT_HERSHEY_SIMPLEX
#         strXY = str(x) + ", " + str(y)
#         cv.putText(img, strXY, (x,y), font, 1, (255, 245,235), 1)
#         cv.imshow("image", img)


img = np. zeros((600, 600,3), np.uint8)
# cv.line(img, (100,200), (230, 400), (230,200,254), 1)

cv.rectangle(img, [170, 150], [450,350], (230,200,254), 2 )
# (300,100) is the (left line-top line) corner and (200,150) is the(right line-bottom line) corner.
# cv.imshow("image", img)

# cv.setMouseCallback("image", click)


points = np.float32([[168, 148], [169,354], [454, 152], [451,353]])
print(img.shape)
height = 600
width = 600

point2 = np.float32([[0,0], [600, 0], [0, height], [width, height]])

matrix = cv.getPerspectiveTransform(points, point2)
outimage = cv.warpPerspective(img, matrix, (width, height))

cv.imshow("image", outimage)
cv.waitKey(0)
cv.destroyAllWindows()