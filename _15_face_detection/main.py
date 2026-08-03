# Detection a face in an image is totally a different matter than recognizing a face in an image which in Detection, all you
# need to do is to decide an image contains a face, or it does not contain a face (classification task)
# while in Recognition not only you have to decide if an image contains a face or not, you also have to recognize whos face that is
from _15_face_detection.pipeline import run
from _15_face_detection.config.paths import IMAGES
from _15_face_detection.config.registery import IMAGES_MAPPING

def get_request():

    images = [f for f in IMAGES.iterdir() if f.is_file()]

    print("What file do you want to perform Face Detection on?")
    for i, image in enumerate(images, start=1):
        print(f"{i}. {image.name}")

    choice = int(input())

    selected_image = images[choice - 1]

    print(f"You have selected: {selected_image}")

    return selected_image

if __name__ == "__main__":
    run(source_image=IMAGES_MAPPING[get_request()])