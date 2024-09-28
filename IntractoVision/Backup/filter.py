import cv2
import numpy as np
# import numpy as nm

cap = cv2.VideoCapture(1)
if cap.isOpened():
    print('True')
else:
    print('0')

while(cap.isOpened()):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Define the HSV range for the red laser color
    # lower_val = np.array([10, 100, 100])
    # upper_val = np.array([255, 255, 255])
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grey', gray_frame)
    # Threshold the grayscale frame to detect the IR LED blob
    _ , thresholded = cv2.threshold(gray_frame, 170, 255, cv2.THRESH_BINARY)
    cv2.imshow('thresh', thresholded)

    # Detect blobs in the thresholded frame
    # keypoints = detector.detect(thresholded)
    # Create a mask to isolate the laser spot
    # mask = cv2.inRange(hsv, lower_val, upper_val)
    # cv2.imshow('thresh', mask)
    # contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('IR LED Tracking', frame)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()