import cv2 as cv

img = cv.imread("Photos/img1.jpg") # Reading an image

cv.imshow("Image", img) # Showing the image variable in a window called "Image"

cv.waitKey(delay=0) # Waiting for infinite amount of time for a key press to close the window

large_img = cv.imread("Photos/img7_large.jpg") # Reading a large image

cv.imshow("Large Image", large_img) # Showing the large image variable in a window called "Large Image"

cv.waitKey(delay=0) # Waiting for infinite amount of time for a key press to close the window