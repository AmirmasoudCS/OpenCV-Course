import cv2 as cv

def threshold(img, threshold=125, maximum=255):

    ret, thresh = cv.threshold(img, threshold, maximum)

    return (ret, thresh)