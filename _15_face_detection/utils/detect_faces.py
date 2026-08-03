import cv2 as cv
from pathlib import Path

from _15_face_detection.utils.greyscale import to_grey
from _15_face_detection.utils.print_cords import print_cords


def detect_faces(image_path: Path, classifier):
    image = cv.imread(str(image_path))

    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    grey_image = to_grey(image)

    faces_rectangle = classifier.detectMultiScale(
        grey_image,
        scaleFactor=1.1,
        minNeighbors=4
    )

    number_of_faces, drawn_image = print_cords(
        image,
        faces_rectangle
    )

    return number_of_faces, drawn_image