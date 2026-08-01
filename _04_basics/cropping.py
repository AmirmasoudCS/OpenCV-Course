import cv2 as cv

def crop(image, start_y, finish_y, start_x, finish_x):

    return image[start_y:finish_y, start_x:finish_x]