import cv2 as cv

img = cv.imread("Photos/img1.jpg") # Reading an image

cv.imshow("Image", img) # Showing the image variable in a window called "Image"

cv.waitKey(delay=0) # Waiting for infinite amount of time for a key press to close the window