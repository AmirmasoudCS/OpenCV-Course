import cv2 as cv
from _15_face_detection.config.constants import (
    GREEN,
    RECTANGLE_THICKNESS,
)

def print_cords(source_image, faces_rect):

    for (x, y, h, w) in faces_rect:
        cv.rectangle(source_image, (x, y), (x+h, y+w), GREEN, RECTANGLE_THICKNESS)


    return(len(faces_rect), source_image)