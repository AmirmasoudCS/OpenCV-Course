from _16_face_recognition.train import create_train
from _16_face_recognition.saver import save
from _16_face_recognition.loader import load_train
import cv2 as cv
import numpy as np

def main():
    overwrite: bool = int(input("Overwrite the train results?\n(0) No    (1) Yes\n"))

    if overwrite:
        features, labels = create_train()
        save(features, labels)

    else:
        features, labels = load_train()

    features = np.array(features, dtype='object')
    labels = np.array(labels)


    face_recognizer = cv.face.LBPHFaceRecognizer_create()

    # Train the Recognizer on the features list and the labels list

    face_recognizer.train(features, labels)

    np.save("config/features.npy", features)
    np.save("config/labels.npy", labels)


        

if __name__ == "__main__":
    main()