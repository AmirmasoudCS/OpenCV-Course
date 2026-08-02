import cv2 as cv

def threshold(img, threshold=125, maximum=255): # Thresholding basically tries to look at an image and binarise the image.
                                                # with threshold=125 and maximum=255 --> pixels that are <125 := 0 and pixels that are >125 := 255

    ret, thresh = cv.threshold(img, threshold, maximum, type=cv.THRESH_BINARY)

    return (ret, thresh)