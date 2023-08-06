                    #     changing resolution of video cam
import cv2 as cv
import numpy as np

# caputring video
cap = cv.VideoCapture(1)

# saving video
forcc = cv.VideoWriter_fourcc(*"XVID")
out = cv.VideoWriter("video.avi", forcc, 20, (640, 480))

# setting HD resolution
# cap.set(3, 1280)
# cap.set(4, 720)
def HD_resol():
    cap.set(3, 1280)
    cap.set(4, 720)
    cap.set(10,0.5)
def fHD_resol():
    cap.set(3, 1920)
    cap.set(4, 1080)
    
HD_resol()


# reading frames and displaying
while(cap.isOpened()):
    ret, frame = cap.read()
    if (ret==True):
        cv.imshow("video",frame)
        # saving frame
        out.write(frame)
        if cv.waitKey(1) & 0xFF == ord('q'):            
            break
        
    else:
        break
cap.release()
cv.destroyAllWindows()