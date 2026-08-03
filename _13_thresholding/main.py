# Thresholding is the binarization of the image, we take an image and turn it into a binary image
# A binary image is an image that pixels are either 0 (black) or 255 (white)
# A very simple thresholding is to take a pixel and compare it to our threshold, if it less than the threshold we assign it to 0 and if it is above it we set it to 255
# We are going to talk about two types of thresholding: (1) Simple Thresholding (2) Adaptive Thresholding

import cv2 as cv



def main():

    image = cv.imread("assets/Photos/boston_park.jpg")

    


if __name__ == "__main__":
    main()