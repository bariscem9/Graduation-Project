import cv2
import numpy as np 

# Web camera
cap = cv2.VideoCapture("video_4k.mp4")
algo = bgsegm.createBackgroundSubstractorMOG()

while True:
    ret,frame1 = cap.read()

    cv2.imshow("Video Original",frame1)

    if cv2.waitKey(1) == 13:
        break

cv2.destroyAllWindows()
cap.release()