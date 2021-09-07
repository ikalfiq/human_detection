#!/usr/bin/env python3 
# detect humans and draw a bounding box around them
# resizing and positioning video output window

import cv2
import imutils
import numpy as np
import argparse

cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Video', 1080, 720)
cv2.moveWindow('Video', 600, 0) # For laptop screen
# cv2.moveWindow('Video', 2700, 0) # For desktop screen

def detect_human(frame):
    hogcv = cv2.HOGDescriptor()
    hogcv.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    bounding_box_cordinates, weights =  hogcv.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 1.03)
    print("Testing")

    person = 1
    for x,y,w,h in bounding_box_cordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f'person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        person += 1

    cv2.putText(frame, 'Status : Detecting ', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.putText(frame, f'Total Persons : {person-1}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.imshow('Video', frame)
    cv2.waitKey(1)


if __name__ == '__main__':
     path = '/home/kalfiq/Desktop/human_detection/humans.mp4'
     capture = cv2.VideoCapture(path)

     if (capture.isOpened()):

         while(True):
             ret, frame = capture.read()

             if (ret == True):
                 gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                 detect_human(gray_frame)

             else:
                capture.release()

