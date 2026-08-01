import cv2 as cv

def dilate(image, kernel_size: tuple[int, int], iterations: int = 1):

    dilated_image = cv.dilate(image, kernel_size, iterations)

    return dilated_image
