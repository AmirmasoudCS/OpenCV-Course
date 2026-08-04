import os
import cv2 as cv

from _16_face_recognition.config.paths import RESULTS_TRAIN
from _16_face_recognition.config.constants import PEOPLE


def load_train():
    features = []
    labels = []

    for filename in os.listdir(RESULTS_TRAIN):
        if not filename.lower().endswith(".jpg"):
            continue

        img_path = os.path.join(RESULTS_TRAIN, filename)
        image = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

        # Remove extension
        name = os.path.splitext(filename)[0]

        # Split into parts
        parts = name.split("_")

        # FirstName_LastName_Number
        person = f"{parts[0]}_{parts[1]}"

        label = PEOPLE.index(person)

        features.append(image)
        labels.append(label)

    return features, labels