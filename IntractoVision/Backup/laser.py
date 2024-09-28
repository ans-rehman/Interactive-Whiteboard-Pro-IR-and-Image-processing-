import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while (1):

    # Take each frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([50, 47, 237])
    upper_red = np.array([225, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)

    m = cv2.moments(mask)
    if m['m00']:
        x = int(m['m10'] / m['m00'])
        y = int(m['m01'] / m['m00'])
        # cv2.circle(mask, (x, y), 10, (255, 255, 255), -1)
        cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)


    cv2.imshow('Track Laser', frame)
    cv2.imshow('mask', mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()