from tools import *
import cv2

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    for bbox in track(frame):
        print(bbox)