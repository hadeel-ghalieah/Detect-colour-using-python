import cv2
import numpy as np

# import the image 
img = cv2.imread('img2.png')

# For color conversion, we use the function cv2.cvtColor(input_image, flag)
# where flag determines the type of conversion.
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# blue range
lower_range = np.array([50,50,50])
upper_range = np.array([130,255,255])

# detect the color
mask = cv2.inRange(hsv, lower_range, upper_range)

# show the result
cv2.imshow('image', img)
cv2.imshow('mask', mask)
cv2.imshow('hsv', hsv)

# end the task
cv2.waitKey(0)
cv2.destroyAllWindows()
