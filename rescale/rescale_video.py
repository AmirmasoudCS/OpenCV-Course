# Displaynig large scaled vidoes and images, which contain a lot of details, can be very slow.
# By rescaling them, we can speed up the display and reduce memory usage, while still preserving the overall appearance of the content.

import cv2 as cv

def rescaleFrame(frame, scale=0.75): # Function to rescale the frame by a given scale factor
    # Images, Videos and Live Video can all be rescaled using this function

    width = frame.shape[1] * scale # frame.shape[1] gives the width of the frame, and we multiply it by the scale factor to get the new width
    height = frame.shape[0] * scale # frame.shape[0] gives the height of the frame, and we multiply it by the scale factor to get the new height

    width = int(width) # Converting the width to an integer
    height = int(height) # Converting the height to an integer

    dimensions = (width, height) # Creating a tuple of the new dimensions

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # Resizing the frame using the new dimensions and returning it


def changeRes(width, height, capture): # Function to change the resolution of the video
    # Live Video

    capture.set(3, width) # Setting the width of the video
    capture.set(4, height) # Setting the height of the video

def main():

    choice = 0
    choice = input("What method of resizing a video do you want to use?\n (1) Rescale the video by a scale factor using the helper function rescaleFrame() .\n (2) Changing the resolution of them using the built in function capture.set method.")

    if choice == "1":
        capture = cv.VideoCapture("Videos/vid1.mp4") # Creating a VideoCapture object to read the video file
        
        while True: # Infinite loop to read and display frames from the video
            
            isTrue, frame = capture.read() # Reading a frame from the video

            resized_frame = rescaleFrame(frame, scale=0.5) # Rescaling the frame by a scale factor of 0.5, take note that rescaling a video by 0.5, reduces the size of it to 0.5 * 0.5 = 0.25, which is a quarter of the original size, if you want to reduce it to half, you should scale = math.sqrt(0.5) instead so sqrt(0.5) * sqrt(0.5) = 0.5, which is half of the original size.

            cv.imshow("Video", frame) # Displaying the original frame
            cv.imshow("Resized Video", resized_frame) # Displaying the rescaled frame

            if cv.waitKey(20) & 0xFF == ord('d'): # Breaking the loop if 'd' is pressed
                break

        capture.release() # Releasing the VideoCapture object
        cv.destroyAllWindows() # Closing all OpenCV windows

    elif choice == "2":

        capture = cv.VideoCapture(0) # Creating a VideoCapture object to read from the webcam
        capture_resized = cv.VideoCapture(0) # Creating another VideoCapture object for the resized video
        changeRes(640, 480, capture) # Changing the resolution of the video to 640x480

        isTrue, frame = capture.read() # Reading a frame from the video
        isTrueResized, frame_resized = capture_resized.read() # Reading a frame from the resized video

        cv.imshow("Video", frame) # Displaying the resized video
        cv.imshow("Resized Video", frame_resized) # Displaying the resized video



if __name__ == "__main__":
    main() # Calling the main function to run the program