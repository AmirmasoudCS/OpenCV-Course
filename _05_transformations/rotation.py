import cv2 as cv


def rotate(image, angle, rotation_point=None):

    (height, width) = image.shape[:2]

    if rotation_point is None: # Assuming by None value for the rotation_point, we are going to rotate along the center
        rotation_point = (width//2, height//2) # Grabbing the middle points of the x-axis and y-axis for center point which is basically in the middle of the image

    rotation_matrix = cv.getRotationMatrix2D(rotation_point, angle, 1.0) # 1.0 is the scaler factor which we are not interested in since we are only rotating

    dimensions = (width, height)

    return cv.warpAffine(image, rotation_matrix, dimensions)