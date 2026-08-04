import os
import cv2 as cv

from _15_face_detection.utils.xml_loader import load_xml
from _15_face_detection.utils.greyscale import to_grey
from _15_face_detection.config.paths import SOURCE
from _15_face_detection.config.constants import SCALE_FACTOR, MINIMUM_NEIGHBOURS

from _16_face_recognition.config.paths import (
    CONFIG,
    VALIDATE,
    RESULTS_VALIDATE,
)
from _16_face_recognition.config.constants import PEOPLE


def main():

    classifier = load_xml(SOURCE / "haar_face.xml")

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read(str(CONFIG / "face_trained.yaml"))

    for person in PEOPLE:

        input_dir = VALIDATE / person
        output_dir = RESULTS_VALIDATE / person

        output_dir.mkdir(parents=True, exist_ok=True)

        for filename in os.listdir(input_dir):

            img_path = input_dir / filename

            img = cv.imread(str(img_path))
            grey = to_grey(img)

            faces_rect = classifier.detectMultiScale(
                grey,
                scaleFactor=SCALE_FACTOR,
                minNeighbors=MINIMUM_NEIGHBOURS,
            )

            for (x, y, w, h) in faces_rect:

                face_roi = grey[y:y+h, x:x+w]

                label, confidence = face_recognizer.predict(face_roi)

                predicted_person = PEOPLE[label]

                cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

                height, width = img.shape[:2]

                font_scale = max(0.5, height / 700)
                thickness = max(1, int(height / 350))

                text = f"{predicted_person} ({confidence:.1f})"
                position = (x, max(30, y - 10))

                # Foreground
                cv.putText(
                    img,
                    text,
                    position,
                    cv.FONT_HERSHEY_COMPLEX,
                    font_scale,
                    (0, 255, 0),
                    thickness,
                    cv.LINE_AA,
                )

            cv.imwrite(str(output_dir / filename), img)


if __name__ == "__main__":
    main()