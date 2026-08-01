import cv2 as cv

def crop(image, start_y, finish_y, start_x, finish_x):
    # Ensure all coordinates are integers
    sy, fy = int(start_y), int(finish_y)
    sx, fx = int(start_x), int(finish_x)
    
    return image[sy:fy, sx:fx]