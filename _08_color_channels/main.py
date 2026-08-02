# All the colored images, consist of different color channels, Red, Green, Blue
# Using OpenCV, you can take an image and split it into its color channels

import cv2 as cv
import numpy as np

def main():

    image = cv.imread("assets/Photos/img7_large.jpg")

    b, g, r = cv.split(image)

    cv.imshow("Blue Channels", b)
    cv.imshow("Green Channels", g)
    cv.imshow("Red Channels", r)

    print(image.shape)
    print(b.shape)
    print(g.shape)
    print(r.shape)
        
    
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()