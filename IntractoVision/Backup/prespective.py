import cv2
import numpy as np

def transform(img,src):
    # Define input image
    # print(input_image.shape)
    # src_points = np.array([[88,66], [203,51], [222,122], [112,145]], dtype=np.float32)
    (tl, tr, br, bl) = src
    src=src.astype(np.float32)
    # Calculate the width of the new image
    width_a = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    width_b = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    max_width = max(int(width_a), int(width_b))

    # Calculate the height of the new image
    height_a = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    height_b = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    max_height = max(int(height_a), int(height_b))

    # Construct the destination points
    dst = np.array([
        [0, 0],
        [max_width - 1, 0],
        [max_width - 1, max_height - 1],
        [0, max_height - 1]
    ], dtype=np.float32)
    # print(dst)
    # print(points)
    # Compute the perspective transform matrix
    matrix = cv2.getPerspectiveTransform(src, dst)

    # Apply the perspective transform to the image
    transformed = cv2.warpPerspective(img, matrix, (max_width, max_height))
    return (transformed,max_width, max_height, dst)
    # cv2.imshow('Input Image', img)
    # # cv2.imshow('homograph Image', output_image)
    # cv2.imshow('prespective Image', transformed)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()