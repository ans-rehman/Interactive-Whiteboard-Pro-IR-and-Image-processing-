import cv2
import numpy as np
import pyautogui
# import wi_prt as wi
import prespective as pt
# scren demension
class ir_detect():
    def __init__(self):
        self.s_width, self.s_height =pyautogui.size()
        # Define the HSV range for the red laser color
        self.lower_val = np.array([0, 0, 240])
        self.upper_val = np.array([180, 255, 255])
        self.pc_cords = [(0,0),(self.s_width-1,0), (self.s_width-1, self.s_height-1), (0, self.s_height-1)]
        self.t=True
        self.cordinates = []
        self.cx = -100
        self.cy = -100
        self.callibration_points()
        self.video_cap()
        # n=100
    def find_position(self, mask):
        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
                # Find the largest contour (IR laser spot)
                largest_contour = max(contours, key=cv2.contourArea)
                # Calculate the centroid of the IR laser spot
                M = cv2.moments(largest_contour)
                if M["m00"] > 0:
                    cord_number=len(self.cordinates)
                    try:
                        self.cx = int(M["m10"] / M["m00"])
                        self.cy = int(M["m01"] / M["m00"])
                    except ZeroDivisionError:
                        return 1
                    if cord_number<4:
                        if cv2.waitKey() & 0xFF == ord('n'):
                            self.cordinates.append((self.cx,self.cy))
                            #  pass
                        elif cv2.waitKey() & 0xFF == ord('u'):
                            #  self.cordinates.pop()
                            return
                else:
                    return 1
        else:
            return 1
    def callibration_points(self):
        # Create a white image covering the entire screen
        # self.self.green_image = np.ones((self.s_height, self.s_width, 3), dtype=np.uint8) * 255
        # Create a blank green image
        self.green_image = np.zeros((self.s_height, self.s_width, 3), dtype=np.uint8)
        self.green_image[:, :] = (0, 255, 0)  # Set color channels to green
        # Add text to the image
        text = "Click On The Blue Spots"
        # text1 = "Clockwise (left-up, right-up, right-bottom, left-bottom)"
        # font = cv2.FONT_HERSHEY_DUPLEX
        font = cv2.FONT_HERSHEY_TRIPLEX
        font_scale = 3
        # font_scale1 = 1
        font_thickness = 8
        # font_thickness1 = 4
        text_color = (0, 0, 0)  # Black color
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
        # text_size1 = cv2.getTextSize(text1, font, font_scale1, font_thickness1)[0]
        text_x = (self.s_width - text_size[0]) // 2
        text_y = (self.s_height - text_size[1]) // 2
        # text_x1 = (self.s_width - text_size1[0]) // 2
        # text_y1 = (self.s_height - text_size1[1]) // 2
        cv2.putText(self.green_image, text, (text_x, text_y), font, font_scale, text_color, font_thickness, cv2.LINE_AA)
        # cv2.putText(self.green_image, text1, (text_x1, text_y1+text_size[1]), font, font_scale1 , text_color, font_thickness1, cv2.LINE_AA)
        # cv2.circle(self.green_image, (10,10), 20, (255, 0, 0), -1)
        # Display the white image in full-screen mode
        for i in range(0,len(self.pc_cords)):
            cv2.circle(self.green_image, self.pc_cords[i], 30, (255, 0, 0), -1)
        xx=100
        yy=100
        cv2.putText(self.green_image, "1", (self.pc_cords[0][0]+xx-30,self.pc_cords[0][1]+yy), font, font_scale-1 , text_color, font_thickness-4, cv2.LINE_AA)
        cv2.putText(self.green_image, "2", (self.pc_cords[1][0]-xx,self.pc_cords[1][1]+yy), font, font_scale-1 , text_color, font_thickness-4, cv2.LINE_AA)
        cv2.putText(self.green_image, "3", (self.pc_cords[2][0]-xx,self.pc_cords[2][1]-yy+10), font, font_scale-1 , text_color, font_thickness-4, cv2.LINE_AA)
        cv2.putText(self.green_image, "4", (self.pc_cords[3][0]+xx-30,self.pc_cords[3][1]-yy+10), font, font_scale-1 , text_color, font_thickness-4, cv2.LINE_AA)
        cv2.namedWindow("White Screen", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("White Screen", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("White Screen", self.green_image)
        # Wait for a key press to exit
    def video_cap(self):
        n=0
        cap = cv2.VideoCapture(1)
        if cap.isOpened():
            print('True')
        else:
            print('0')
        while (cap.isOpened()):
            if cv2.waitKey(1) & 0xFF == ord('d'):
                self.cordinates = []
            # Capture a frame from the webcam
            ret, frame = cap.read()
            n=n+1
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # Create a mask to isolate the laser spot
            mask = cv2.inRange(hsv, self.lower_val, self.upper_val)
        # threshold
            # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Threshold the grayscale frame to detect the IR LED blob
            # _ , mask = cv2.threshold(gray_frame, 30, 255, cv2.THRESH_BINARY)
            cv2.imshow('thresh', mask)
            if n<=30:
                continue
            if len(self.cordinates)<4:
                self.find_position(mask)
                cv2.imshow("White Screen", self.green_image)
                if len(self.cordinates)==4:
                    cv2.destroyWindow("White Screen")
                # print(self.cordinates)
            elif len(self.cordinates)==4:
                src_points = np.array([i for i in self.cordinates], dtype=np.int32)
                transformed_img, width, height, dst = pt.transform(mask,src_points)
                c=self.find_position(transformed_img)
                # point=[self.cx,self.cy]
                fx=int(((self.s_width/width)*self.cx))
                fy =int(((self.s_height/height)*self.cy))
                # Reshape the vertices to fit the OpenCV format
                vertices = src_points.reshape((-1, 1, 2))
                # Draw the trapezoid on the image
                cv2.polylines(frame, [vertices], isClosed=True, color=(0, 255, 0), thickness=2)
                dst=dst.astype(np.int32)
                result = cv2.pointPolygonTest(dst, (self.cx,self.cy), measureDist=False)
                # Check the result
                if c:
                    self.t=True
                    pyautogui.mouseUp()
                else:
                    if result >= 0:
                        cv2.circle(frame, (self.cx,self.cy), 8, (0, 255, 0), -1)
                        self.t=False
                        # pyautogui.moveTo((fx,fy))
                        pyautogui.mouseDown(fx,fy)
                    elif result<0:
                        cv2.circle(frame, (self.cx,self.cy), 8, (0, 0, 255), -1)
                        self.t=True
                        pyautogui.mouseUp()
                    cv2.imshow('transformed mask', transformed_img)
            cv2.imshow('IR LED Tracking', frame)
            # Exit the loop if the 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    # Release the webcam and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()