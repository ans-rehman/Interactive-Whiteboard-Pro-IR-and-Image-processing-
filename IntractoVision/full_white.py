# import numpy as np
# import cv2

# # Get screen resolution
# screen_width, screen_height = 1920, 1080  # Adjust these values to match your screen resolution

# # Create a white image covering the entire screen
# white_image = np.ones((screen_height, screen_width, 3), dtype=np.uint8) * 255

# # Display the white image in full-screen mode
# cv2.text()
# cv2.namedWindow("White Screen", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("White Screen", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# cv2.imshow("White Screen", white_image)

# # Wait for a key press to exit
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import numpy as np
import cv2
import pyautogui

screen_width, screen_height=pyautogui.size()
# Get screen resolution
# screen_width, screen_height = 1920, 1080  # Adjust these values to match your screen resolution

# Create a blank green image
green_image = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)
green_image[:, :] = (0, 255, 0)  # Set color channels to green

# Add blue text to the image
text = "Blue Text"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.5
font_thickness = 2
text_color = (255, 0, 0)  # Blue color
text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
text_x = (green_image.shape[1] - text_size[0]) // 2
text_y = (green_image.shape[0] + text_size[1]) // 2
cv2.putText(green_image, text, (text_x, text_y), font, font_scale, text_color, font_thickness, cv2.LINE_AA)

# Display the image
cv2.imshow("Green Image with Blue Text", green_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
