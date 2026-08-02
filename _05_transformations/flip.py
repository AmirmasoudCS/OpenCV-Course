import cv2 as cv

def flip(image, flip_code):   # flip_code can take three values of 1, 0, -1
                                # 0 --> flips over the x-axis
                                # 1 --> flips over the y-axis
                                # -1 --> flips over both axis
    return cv.flip(image, flip_code)