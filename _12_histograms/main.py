# Histograms allow you to visualize the distribution of pixel intensities in an image (colored or greyscale doesn't matter)

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def main():

    choice = input("(1) Greyscaled Histogram.\n(2) Masked Greyscaled Histogram.\n(3) Coloured Histogram.\n")

    image = cv.imread("assets/Photos/boston_park.jpg")
    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


    if choice == "1":

        cv.imshow("Grey Image", grey_image)
        
        # Greyscale Histogram
    
        grey_histogram = cv.calcHist([grey_image], [0], None, [256], [0, 256])      # Images should be passed as a list, second argument is the index of number of channels which in terms of greyscale images is 1, third argument is a mask if 
                                                                                    # we want to compute a masked area histogram for, fourth parameter is the number of bins we want to compute the histogram on, and last argument is the range of pixels
        plt.figure()
        plt.title("Greyscale Histogram")
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")
        plt.xlim([0, 256])
        plt.ylim([0, 5000])
        plt.plot(grey_histogram)
        plt.show()
        

    elif choice == "2":

        # We can also use mask to compute the pixel density in a particular place in an image using the mask
    
        mask = np.zeros(grey_image.shape[:2], dtype="uint8")
        cv.circle(mask, (grey_image.shape[1] // 2, grey_image.shape[0] // 2), 75, 255, -1)

        masked_image = cv.bitwise_and(grey_image, grey_image, mask=mask)
        cv.imshow("Masked Image", masked_image)

        mask_histogram = cv.calcHist(images=[grey_image], channels=[0], mask=mask , ranges=[0, 256], histSize=[256])
    
        plt.figure()
        plt.title("Greyscal Masked Histogram")
        plt.xlabel("Bin")
        plt.ylabel("# of Pixels")
        plt.xlim([0, 256])
        plt.ylim([0, 5000])
        plt.plot(mask_histogram)
        plt.show()

    elif choice == "3":

        cv.imshow("Original Image", image)

        plt.figure()
        plt.title("Coloured Histogram")
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")

        colours = ('b', 'g', 'r')

        for i, col in enumerate(colours):
            hist = cv.calcHist([image], [i], None, 256, [0, 256])
            plt.plot(hist)
            plt.xlim([0, 256])
            plt.ylim([0, 4000])

        plt.show()
        

    else:
        print("Wrong input!")
        return

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
    