from _15_face_detection.utils.greyscale import to_grey
from _15_face_detection.utils.xml_loader import load_xml
from _15_face_detection.config.paths import SOURCE
from _15_face_detection.config.constants import (
    SCALE_FACTOR,
    MINIMUM_NEIGHBOURS
)


def run(source_image):

    grey_image = to_grey(source=source_image)

    classifier = load_xml(SOURCE / "haar_face.xml")

    faces_rectangle = classifier.detectMultiScale(grey_image, scaleFactor=SCALE_FACTOR, minNeighbors=MINIMUM_NEIGHBOURS)

    print(f"Number of faces found: {len(faces_rectangle)}.")
