import cv2 as cv

def resize(image, new_size: tuple[int, int] = (500, 500)):

    resized_image = cv.resize(image, new_size)  # There are different interpolation options:
                                                # (1) cv.INTER_AREA --> Shrinking the images
                                                # (2) cv.INTER_LINEAR --> Enlarging the images
                                                # (3) cv.INTER_CUBIC --> Slowest of them all but better results in the end
    return resized_image    