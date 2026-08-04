import numpy as np
import cv2 as cv
from _15_face_detection.utils.xml_loader import load_xml
from _15_face_detection.config.paths import SOURCE
from _16_face_recognition.config.paths import CONFIG
from _16_face_recognition.config.constants import PEOPLE


def main():

    classifier = load_xml(SOURCE / "haar_face.xml")

    features = np.load(CONFIG / "features.npy")
    labels = np.load(CONFIG / "labels.npy")

    face_recognizer = cv.face.LBPHFaceRecognizer_creat()

    face_recognizer.read(CONFIG / "face_trained.yaml")


if __name__ == "__main__":
    main()