                        # Splitting frames

import cv2 as cv
import numpy as np

cap = cv.VideoCapture("resources/video.mp4")


def split_frames():
    frameNr = 0

    while (True):
        ret, frame = cap.read()
        if ret:
            cv.imwrite(f"resources/frames/frame_{frameNr}.jpg", frame)
        else:
            break
        frameNr = frameNr+1
    cap.release()
    
split_frames()