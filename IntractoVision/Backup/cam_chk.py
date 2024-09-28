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
    
    # # frame = cv2.flip(frame,1) #using laptops webcam mirror selfie
    # blue_channel, green_channel, red_channel = frame[:,:,0], frame[:,:,1], frame[:,:,2]
    # blue_channel = 
    # # Display the individual color channels
    # cv2.imshow('Blue Channel', blue_channel)
    # cv2.imshow('Green Channel', green_channel)
    # cv2.imshow('Red Channel', red_channel)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Threshold the grayscale frame to detect the IR LED blob
    _ , mask = cv2.threshold(gray_frame, 240, 255, cv2.THRESH_BINARY)
    # mask = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # cv2.imshow('thresh', mask)
    # Convert the frame to grayscale
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # cv2.imshow('frame_orignal', frame)
    # Define the HSV range for the red laser color
    # lower_val = np.array([0, 0, 200])
    # upper_val = np.array([180, 255, 255])
    # Create a mask to isolate the laser spot
    # mask = cv2.inRange(hsv, lower_val, upper_val)
    # contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('thresh', mask)
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


# import cv2
# import numpy as np
 
# def nothing(x):
#     pass

# # Open the camera
# cap = cv2.VideoCapture(0) 
 
# # Create a window
# cv2.namedWindow('image')
 
# # create trackbars for color change
# cv2.createTrackbar('lowH','image',0,179,nothing)
# cv2.createTrackbar('highH','image',179,179,nothing)
 
# cv2.createTrackbar('lowS','image',0,255,nothing)
# cv2.createTrackbar('highS','image',255,255,nothing)
 
# cv2.createTrackbar('lowV','image',0,255,nothing)
# cv2.createTrackbar('highV','image',255,255,nothing)
 
# while(True):
#     ret, frame = cap.read()
 
#     # get current positions of the trackbars
#     ilowH = cv2.getTrackbarPos('lowH', 'image')
#     ihighH = cv2.getTrackbarPos('highH', 'image')
#     ilowS = cv2.getTrackbarPos('lowS', 'image')
#     ihighS = cv2.getTrackbarPos('highS', 'image')
#     ilowV = cv2.getTrackbarPos('lowV', 'image')
#     ihighV = cv2.getTrackbarPos('highV', 'image')
    
#     # convert color to hsv because it is easy to track colors in this color model
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     lower_hsv = np.array([ilowH, ilowS, ilowV])
#     higher_hsv = np.array([ihighH, ihighS, ihighV])
#     # Apply the cv2.inrange method to create a mask
#     mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
#     # Apply the mask on the image to extract the original color
#     frame = cv2.bitwise_and(frame, frame, mask=mask)
#     cv2.imshow('image', frame)
#     # Press q to exit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()