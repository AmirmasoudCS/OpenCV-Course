# Using the previously learned bitwise operations we can perform masking in OpenCV
# Masking allows us to focus on certain parts of the image that we like to focus on
# e.g. you have a picture of people and you want to focus on their faces

import cv2 as cv
import numpy as np


def main():

    image = cv.imread("assets/Photos/img4.jpg")
    cv.imshow("Original Image", image)

    blank = np.zeros(image.shape[:2], dtype="uint8") # The dimensions of the mask has to be of the dimensions of the image

    mask = cv.circle(blank, (image.shape[1]//2, image.shape[0]//2), 100, 255, -1)

    cv.imshow("Mask", mask)
    

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()