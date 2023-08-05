                                        # writing text on video
# import libraries
import cv2 as cv
import numpy as np

cap = cv.VideoCapture("resources/video.mp4")


while(cap.isOpened()):
    ret, frame = cap.read()
    if (ret == True):
        test = "testing this text onn video"
        cv.putText(frame,test,(0,20),cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,255, 255), 1, cv.LINE_AA)
        # cv.putText(source, text,cordinates,font, fontscae, color,thicknnes, lineType)
        
        
        
        cv.imshow("video", frame)
        if cv.waitKey(39) &0xFF == ord('q'):
            break
        
    else:
        break

cap.release()
cv.destroyAllWindows()