import cv2 as cv
import numpy as np
# Translation is shifting an image along the X and Y axis ( up, down, left, right) or any combination of them

def translate(image, x, y): # x and y are number of pixels you want to shift along the x-axis and y-axis

        # +x --> Right
        # +y --> Down
        # -x --> Left
        # -y --> Up


    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])

    dimensions = (image.shape[1], image.shape[0]) # image.shape[1] = width of the image and image.shape[0] = height of the image

    return cv.warpAffine(image, translation_matrix, dimensions)