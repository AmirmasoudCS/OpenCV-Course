import cv2 as cv
from pathlib import Path

from _15_face_detection.utils.xml_loader import load_xml
from _15_face_detection.utils.detect_faces import detect_faces
from _15_face_detection.utils.saver import save_all
from _15_face_detection.config.paths import SOURCE
from _15_face_detection.config.constants import (
    SCALE_FACTOR,
    MINIMUM_NEIGHBOURS,
)


def run(source_image_path: Path | None, all: bool = False):

    # Load the classifier only once
    classifier = load_xml(SOURCE / "haar_face.xml")

    if not all:

        number_of_faces, drawn_image = detect_faces(
            image_path=source_image_path,
            classifier=classifier
        )

        if number_of_faces == 0:
            print("No faces were detected.")
        else:
            print(f"Number of faces detected: {number_of_faces}")

        cv.imshow("Detected Face", drawn_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    else:
        save_all(classifier)