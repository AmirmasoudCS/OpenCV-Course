import cv2 as cv

def to_grey(source):
    return cv.cvtColor(source, cv.COLOR_BGR2GRAY)