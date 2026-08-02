import cv2 as cv

def threshold(img, threshold=125, maximum=255): # Thresholding basically tries to look at an image and binarise the image.

    ret, thresh = cv.threshold(img, threshold, maximum)

    return (ret, thresh)