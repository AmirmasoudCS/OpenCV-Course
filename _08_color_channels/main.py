# All the colored images, consist of different color channels, Red, Green, Blue
# Using OpenCV, you can take an image and split it into its color channels

import cv2 as cv
import numpy as np

def main():

    image = cv.imread("assets/Photos/img7_large.jpg")

    b, g, r = cv.split(image)

    cv.imshow("Blue Channels", b)   # These images are shown in greyscael, and the meaning of pixels in greyscale
    cv.imshow("Green Channels", g)  # is that wherever it is lighter, the density of that color in that specific
    cv.imshow("Red Channels", r)    # area is higher, and when it is darker, the absence of that color

    print(image.shape) # The third argument that gets printed, is the number of its colored channels
    print(b.shape)     # There is no third argument in the shape of the blue, green, and red colors since they only represent one color
    print(g.shape)
    print(r.shape)
        
    
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()