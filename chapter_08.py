import cv2 as cv

img = cv.imread("resources/img.jpeg")

cv.imshow("tasveer",img)

k = cv.waitKey() &0xFF

if (k==27):     # 27 is equal to Esc in ASCII
    cv.destroyAllWindows()
elif (k == ord("s")):
    cv.imwrite("pic.png", img)