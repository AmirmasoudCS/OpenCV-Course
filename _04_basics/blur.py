import cv2 as cv

def blur(image):

    blured_image = cv.GaussianBlur(src=image, ksize=(3,3), borderType=cv.BORDER_DEFAULT) # ksize is the kernel size that we are going to apply the Gaussian blur on which needs to be an odd by odd set of numbers: (odd, odd)

    return blured_image