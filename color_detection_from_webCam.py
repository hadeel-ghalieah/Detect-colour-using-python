import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    
    # convert the BGR space color to HSV space color
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # determining the range for the red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask= red_mask)

    # determining the range for the blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    
    # determining the range for the green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    
    cv2.imshow("Frame", frame)
    
    #cv2.imshow("Red mask", red_mask)
    #cv2.imshow('Red', red)

    cv2.imshow("Blue mask", blue_mask)
    cv2.imshow('Blue', blue)

    #cv2.imshow("green mask", green_mask)
    #cv2.imshow('green', green)
    

    key = cv2.waitKey(1) & 0xff
    
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()











