import cv2 as cv

from _15_face_detection.utils.greyscale import to_grey
from _15_face_detection.utils.xml_loader import load_xml
from _15_face_detection.utils.print_cords import print_cords
from _15_face_detection.config.paths import SOURCE
from _15_face_detection.config.constants import (
    SCALE_FACTOR,
    MINIMUM_NEIGHBOURS
)


def run(source_image):

    grey_image = to_grey(source=source_image)

    classifier = load_xml(SOURCE / "haar_face.xml")

    faces_rectangle = classifier.detectMultiScale(grey_image, scaleFactor=SCALE_FACTOR, minNeighbors=MINIMUM_NEIGHBOURS)

    number_of_faces, drawn_image = print_cords(source_image, faces_rectangle)

    print("Number of faces detected in the source image:", number_of_faces)
    cv.imshow("Detected Face", drawn_image)