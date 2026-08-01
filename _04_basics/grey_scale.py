import cv2 as cv


def to_grey(image):
    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return grey_image

