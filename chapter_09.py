                                          # converting video into gray

# importing libraries
import cv2 as cv

# importing a video
cap = cv.VideoCapture(1)

# reading the video
# loop to capture the each frame of video
while(cap.isOpened()):   # return True if file opened, false if not opened
    ret, frame = cap.read()
    print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    
    #conversion to gray
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # playing the video
    cv.imshow("gray", gray)
        
    if cv.waitKey(39) &0xFF == ord("q"):
        break

cap.release() # to release all the resources
cv.destroyAllWindows()
    
    
    
# cap.read return two values: 
    # 1. If the frame is available or not (true or false) and save it in ret variable
    # 2. If True then return the frame and save it in frame variable