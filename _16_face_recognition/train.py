import os
import cv2 as cv
import numpy as np

from config.constants import PEOPLE
from config.paths import TRAIN
from _15_face_detection.utils.xml_loader import load_xml
from _15_face_detection.utils.detect_faces import detect_faces
from _15_face_detection.utils.greyscale import to_grey
from _15_face_detection.config.paths import SOURCE
from _15_face_detection.config.constants import SCALE_FACTOR, MINIMUM_NEIGHBOURS

def create_train():

    features = []
    labels = []


    for person in PEOPLE:
        path = os.path.join(TRAIN, person)
        label = PEOPLE.index(person)

        for img in os.lisdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            grey = to_grey(img_array)
            classifier = load_xml(SOURCE / "haar_face.xml")

            faces_rect = classifier.detectMultiScale(grey, scaleFactor=SCALE_FACTOR, minNeighbors=MINIMUM_NEIGHBOURS)

            for (x, y, w, h) in faces_rect:
                faces_roi = grey[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

    return features, labels
