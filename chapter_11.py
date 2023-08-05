# setting brightness, height and width of camera and video

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)
forcc = cv.VideoWriter_fourcc(*"XVID")

out = cv.VideoWriter("video.mp4", forcc, 20, (640, 480))

# In opencv every propert is associated with a number. for example height = 4

# cap.set(10, 400)  # 10 is the key of brightness, enhance brightness 50 percent

# Setting width of the video
cap.set(3, 900)
# cap.set(cap.get(cv.CAP_PROP_FRAME_WIDTH), 300)


# setting height of the video
cap.set(4, 800) 
# cap.set(cap.get(cv.CAP_PROP_FRAME_HEIGHT), 300)  

while(cap.isOpened()):
    ret, frame = cap.read()
    if (ret==True):
        cv.imshow("vidoe",frame)
        out.write(frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()