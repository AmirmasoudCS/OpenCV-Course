# Histograms allow you to visualize the distribution of pixel intensities in an image (colored or greyscale doesn't matter)

import cv2 as cv
import matplotlib.pyplot as plt


def main():

    image = cv.imread("assets/Photos/boston_park.jpg")

    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("Grey Image", grey_image)

    # Greyscale Histogram

    grey_histogram = cv.calcHist([grey_image], [0], None, [256], [0, 256])      # Images should be passed as a list, second argument is the index of number of channels which in terms of greyscale images is 1, third argument is a mask if 
                                                                                # we want to compute a masked area histogram for, fourth parameter is the number of bins we want to compute the histogram on, and last argument is the range of pixels
    plt.figure()
    plt.title("Greyscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(grey_histogram)
    plt.xlim([0.256])
    plt.show()


    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
    