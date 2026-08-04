import os
import cv2 as cv
from _16_face_recognition.config.paths import RESULTS_TRAIN

def save(features, labels, people):
    os.makedirs(RESULTS_TRAIN, exist_ok=True)

    counters = {person: 0 for person in people}

    for feature, label in zip(features, labels):
        person = people[label]
        filename = f"{person}_{counters[person]}.jpg"
        cv.imwrite(os.path.join(RESULTS_TRAIN, filename), feature)
        counters[person] += 1