import cv2 as cv

def erode(image, kernel_size: tuple[int, int] = (3,3), iterations: int = 1 ):

    eroded_image = cv.erode(image, kernel_size, iterations)

    return eroded_image