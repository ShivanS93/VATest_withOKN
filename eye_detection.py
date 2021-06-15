#!python3
# eye_detection.py - detect eyes using webcam
# tutorial: https://www.roytuts.com/real-time-eye-detection-in-webcam-using-python-3/

import cv2
import math
import numpy as np

def main():

    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    # grab the reference to the webcam
    #try:
    vs = cv2.VideoCapture(13)
    print(vs)


    while True:
        ret, frame = vs.read()

        if frame is None:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        faces = faceCascade.detectMultiScale(frame)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eyeCascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

            cv2.imshow("Video", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord('q') or key == 27:
                break


    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
