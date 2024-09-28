import numpy as np
import cv2
import prespective as tm


# Create a black image
image = np.zeros((600, 600, 3), dtype=np.uint8)

# Define the coordinates of the trapezoid's vertices
# vertices = np.array([[100, 100], [300,70], [350, 300], [50, 400]], dtype=np.int32)
vertices = np.array([[138 , 93], [522, 118], [542, 397], [149, 383]], dtype=np.int32)

# Reshape the vertices to fit the OpenCV format
vertices = vertices.reshape((-1, 1, 2))
print(vertices)
# Draw the trapezoid on the image
cv2.polylines(image, [vertices], isClosed=True, color=(0, 255, 0), thickness=2)

src_points = np.array([[88,66], [203,51], [222,122], [112,145]], dtype=np.float32)
point=[100,100]
result = cv2.pointPolygonTest(vertices, point, measureDist=False)

# Check the result
if result > 0:
    cv2.circle(image, point, 8, (0, 255, 0), -1)
    print("Point is inside the polygon")
elif result < 0:
    cv2.circle(image, point, 8, (0, 0, 255), -1)
    print("Point is outside the polygon")
else:
    cv2.circle(image, point, 8, (255, 0, 0), -1)
    print("Point is on the edge of the polygon")
# img=cv2.imread('images1.jpeg')
# transformed=tm.transform(img,src_points)
# Display the image
cv2.imshow('Trapezoid', image)
# cv2.imshow('Input Image', img)
# # cv2.imshow('homograph Image', output_image)
# cv2.imshow('prespective Image', transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
