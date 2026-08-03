from pathlib import Path
import cv2 as cv

from _15_face_detection.config.paths import IMAGES, OUTPUTS
from _15_face_detection.utils.detect_faces import detect_faces

OUTPUTS.mkdir(parents=True, exist_ok=True)

def save_all(classifier):

    images = sorted(
        [image for image in IMAGES.iterdir() if image.is_file()]
    )

    for image_path in images:

        number_of_faces, drawn_image = detect_faces(
            image_path=image_path,
            classifier=classifier
        )

        output_path = OUTPUTS / image_path.name

        cv.imwrite(str(output_path), drawn_image)

        print(
            f"{image_path.name}: {number_of_faces} face(s) detected."
        )

    print("\nAll images have been processed successfully.")