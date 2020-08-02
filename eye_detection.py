#!python3
# eye_detection.py - detect eyes using webcam
# tutorial: https://www.roytuts.com/real-time-eye-detection-in-webcam-using-python-3/

import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# grab the reference to the webcam
vs = cv2.VideoCapture(0)