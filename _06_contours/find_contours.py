import cv2 as cv

def find_contours(image):
    contours, hierarchies = cv.findContours(image, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    return (contours, hierarchies)