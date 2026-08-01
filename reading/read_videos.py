import cv2 as cv

capture = cv.VideoCapture("Videos/vid1.mp4") # Reading a video file from a path given to it

# You can also use a webcam by passing 0 or 1 to the VideoCapture function: cv.VideoCapture(0) or cv.VideoCapture(1)

while True:

    isTrue, frame = capture.read() # Reading the video frame by frame

    cv.imshow("Video", frame) # Displaying the video frame by frame

    if cv.waitKey(20) & 0xFF==ord('d'): # Press 'd' to exit the video
        break

capture.release() # Releasing the video capture object
cv.destroyAllWindows() # Destroying all the windows opened by OpenCV

# At the end of the vidoe, the video will be closed and an error will be thrown.
#  more specifically an assertion -215 error, which basically means the video ran out of frames.
#  To avoid this, we can add a check to see if the video has ended and break the loop if it has.