import cv2 as cv

def find_edge(image, th1, th2):

    canny = cv.Canny(image, th1, th2) # 125 and 175 are respectively threshold1 and threshold2 values

    return canny