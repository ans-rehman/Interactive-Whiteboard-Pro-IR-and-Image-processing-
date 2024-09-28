import cv2
import numpy as np

# Define source and destination points (4 pairs)
src_points = np.array([[88,66], [203,51], [222,122], [112,145]], dtype=np.float32)
# src_points = np.array([[123,57], [190,82], [162,163], [95,140]], dtype=np.float32)
dst_points = np.array([[10, 0], [125, 0], [125, 90], [10, 90]], dtype=np.float32)



# Compute homography matrix
homography_matrix, _ = cv2.findHomography(src_points, dst_points)
# prespective_matrix= cv2.getPerspectiveTransform(src_points, dst_points)

# Define input image
input_image = cv2.imread('images1.jpeg')
print(input_image.shape)

# fro image extraction
image = np.zeros((183, 275, 3), dtype=np.uint8)

# Define the coordinates of the trapezoid's vertices
vertices = np.array([[88,66], [203,51], [222,122], [112,145]], dtype=np.int32)

# Reshape the vertices to fit the OpenCV format
vertices = vertices.reshape((-1, 1, 2))


# Draw the trapezoid on the image
cv2.fillPoly(image, [vertices], color=(255, 255, 255),)

image_extract = cv2.bitwise_and(image,input_image)

# Apply homography transformation
output_image = cv2.warpPerspective(image_extract, homography_matrix, (input_image.shape[1], input_image.shape[0]))
# output_image1 = cv2.warpPerspective(image_extract, prespective_matrix, (input_image.shape[1], input_image.shape[0]))

input_image=cv2.circle(input_image, (222,122), 5, (0, 255, 0), -1)
# left upper (123,57), (88,66)
# right upper (190,82), (203,51)
# right bottom (162,163), (222,122)
# left bottom (95,140),  (112,145)

# Display input and output images
cv2.imshow('mask', image)
cv2.imshow('extract', image_extract)

cv2.imshow('Input Image', input_image)
cv2.imshow('homograph Image', output_image)
# cv2.imshow('prespective Image', output_image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
