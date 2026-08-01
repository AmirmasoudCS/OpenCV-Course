# Displaynig large scaled vidoes and images, which contain a lot of details, can be very slow.
# By rescaling them, we can speed up the display and reduce memory usage, while still preserving the overall appearance of the content.

import cv2 as cv

img = cv.imread("Photos/img1.jpg")
cv.imshow("Image", img)
cv.waitKey(0)

def rescaleFrame(frame, scale=0.75): # Function to rescale the frame by a given scale factor

    width = frame.shape[1] * scale # frame.shape[1] gives the width of the frame, and we multiply it by the scale factor to get the new width
    height = frame.shape[0] * scale # frame.shape[0] gives the height of the frame, and we multiply it by the scale factor to get the new height

    width = int(width) # Converting the width to an integer
    height = int(height) # Converting the height to an integer

    dimensions = (width, height) # Creating a tuple of the new dimensions

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # Resizing the frame using the new dimensions and returning it