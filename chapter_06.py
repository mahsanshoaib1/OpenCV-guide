                                        # reading the video
# importing libraries
import cv2 as cv

# importing a video
cap = cv.VideoCapture("resources/video.mp4")

# Indicator: checking if there is an error while loading the video
if (cap.isOpened() == False):
    print("video not found")

# reading and playing the video
# loop to capture the each frame of video
while(cap.isOpened()):
    ret, frame = cap.read()
    if (ret == True):
        cv.imshow("video", frame)
        if cv.waitKey(39) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()