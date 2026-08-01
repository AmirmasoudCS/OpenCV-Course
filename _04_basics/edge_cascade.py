import cv2 as cv

def find_edge(image):

    canny = cv.Canny(image, 125, 175) # 125 and 175 are respectively threshold1 and threshold2 values

    return canny