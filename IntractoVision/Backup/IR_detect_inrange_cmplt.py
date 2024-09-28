import cv2
import numpy as np
import pyautogui
# import wi_prt as wi
import prespective as pt
# scren demension
class ir_detect():
    def __init__(self):
        self.s_width, self.s_height =pyautogui.size()
        self.t=True
        self.cordinates = []
        self.cx = -100
        self.cy = -100
        self.video_cap()
        # n=100
    def find_position(self,mask, frame):
        # global self.cordinates
        # global self.cx,self.cy
        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
                # Find the largest contour (IR laser spot)
                largest_contour = max(contours, key=cv2.contourArea)
                # Calculate the centroid of the IR laser spot
                M = cv2.moments(largest_contour)
                if M["m00"] > 0:
                    try:
                        self.cx = int(M["m10"] / M["m00"])
                        self.cy = int(M["m01"] / M["m00"])
                    except ZeroDivisionError:
                        return 1
                    if len(self.cordinates)<4:
                        if cv2.waitKey() & 0xFF == ord('n'):
                            self.cordinates.append((self.cx,self.cy))
                            cv2.circle(frame, (self.cx,self.cy), 8, (0, 255, 0), -1)
                            #  pass
                        elif cv2.waitKey() & 0xFF == ord('u'):
                            #  self.cordinates.pop()
                            return
                else:
                    return 1
        else:
            return 1
        
    def video_cap(self):
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            print('True')
        else:
            print('0')
        while (cap.isOpened()):
            if cv2.waitKey(1) & 0xFF == ord('d'):
                self.cordinates = []
            # Capture a frame from the webcam
            ret, frame = cap.read()
            # c_height , c_width, _ = frame.shape()

        # threshold
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # cv2.imshow('grey', gray_frame)
            # Threshold the grayscale frame to detect the IR LED blob
            _ , mask = cv2.threshold(gray_frame, 230, 255, cv2.THRESH_BINARY)

        # hsv inrange
            # frame = cv2.flip(frame,1) #using laptops webcam mirror selfie
            # Convert the frame to hsv
            # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # cv2.imshow('frame_orignal', frame)
            # Define the HSV range for the red laser color
            # lower_val = np.array([50, 47, 237])
            # upper_val = np.array([225, 255, 255])
            # Create a mask to isolate the laser spot
            # mask = cv2.inRange(hsv, lower_val, upper_val)
            cv2.imshow('thresh', mask)

            if len(self.cordinates)<4:
                self.find_position(mask, frame)
                # print(self.cordinates)
            
            elif len(self.cordinates)==4:
                src_points = np.array([i for i in self.cordinates], dtype=np.int32)
                transformed_img, width, height, dst = pt.transform(mask,src_points)
                c=self.find_position(transformed_img, frame)
                # point=[self.cx,self.cy]
                fx=int(((self.s_width/width)*self.cx))
                fy =int(((self.s_height/height)*self.cy))
                # Reshape the vertices to fit the OpenCV format
                # dsself.t=dst.astype(np.int32)
                vertices = src_points.reshape((-1, 1, 2))
                # print('vertices',vertices)
                # Draw the trapezoid on the image
                cv2.polylines(frame, [vertices], isClosed=True, color=(0, 255, 0), thickness=2)
                dst=dst.astype(np.int32)
                # vertices = dst.reshape((-1, 1, 2))
                result = cv2.pointPolygonTest(dst, (self.cx,self.cy), measureDist=False)
                # print(result)
                # print(dst)
                # Check the result
                if c:
                    self.t=True
                    pyautogui.mouseUp()
                else:
                    if result >= 0:
                        # print(fx,fy)
                        cv2.circle(frame, (self.cx,self.cy), 8, (0, 255, 0), -1)
                        self.t=False
                        # pyautogui.moveTo((fx,fy))
                        pyautogui.mouseDown(fx,fy)
                    elif result<0:
                        cv2.circle(frame, (self.cx,self.cy), 8, (0, 0, 255), -1)
                        # if self.t==False:
                        self.t=True
                        pyautogui.mouseUp()
                        # print("Point is outside the polygon")
                    # cv2.rectangle(frame,self.cordinates[0],self.cordinates[1], color=(0,255,0), thickness=5)
                    # print(self.cordinates[0][0])
                    cv2.imshow('transformed mask', transformed_img)
            cv2.imshow('IR LED Tracking', frame)

            # Exit the loop if the 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release the webcam and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

# if __name__ == "__main__":
#     ir_detect()