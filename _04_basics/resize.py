import cv2 as cv

def resize(image, new_size: tuple[int, int] = (500, 500)):

    resized_image = cv.resize(image, new_size)

    return resized_image