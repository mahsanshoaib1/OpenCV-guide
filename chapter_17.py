                                        # handling mouse events and finding x, y parameters of a specific location on an image

# events = [i for i in dir(cv) if "EVENT" in i]
import cv2 as cv
import numpy as np
def mouse_event(event, x, y, param, flags):
    if event == cv.EVENT_LBUTTONDBLCLK:
        print(x, ", " , y)
        font = cv.FONT_HERSHEY_SIMPLEX()
        strXY = str(x) + ", ", str(y)
        cv.putText(img, strXY, (x,y), font, 1, (255, 245,235), 1)
        cv.imshow("image", img)
        
                         #  finding bgr channel names
        if event == cv.EVENT_RBUTTONDBLCLK():
            blue = img[x,y, 0]
            green = img[x,y, 1]
            red = img[x,y,2]
            strcolr = str(blue) + ", " + str(green) + ", " + str(red)
            font = cv.FONT_HERSHEY_SIMPLEX()
            cv.putText(img, strcolr, (x,y), font, 1 ,  (245, 234, 255), 1)
            cv.imshow("image", img)

img = np.zeros((600, 600, 3), np.uint8)
cv.imshow("image", img)
cv.setMouseCallback("image", mouse_event)

cv.waitKey(0)
cv.destroyAllWindows()




    