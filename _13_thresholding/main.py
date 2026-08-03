# Thresholding is the binarization of the image, we take an image and turn it into a binary image
# A binary image is an image that pixels are either 0 (black) or 255 (white)
# A very simple thresholding is to take a pixel and compare it to our threshold, if it less than the threshold we assign it to 0 and if it is above it we set it to 255
# We are going to talk about two types of thresholding: (1) Simple Thresholding (2) Adaptive Thresholding

import cv2 as cv



def main():

    image = cv.imread("assets/Photos/boston_park.jpg")
    cv.imshow("Original Image", image)

    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Simple Thresholding

    threshold, thresh = cv.threshold(grey_image, 150, 255, cv.THRESH_BINARY)    # (soruce_image, threshold, maximum_value, thresholding_type)
                                                                                # It takes every pixel and compares it to threshold value:
                                                                                # if pixel_value < threshold_value --> pixel_value := 0
                                                                                # if pixel_value > threshold_value --> pixel_value := maximum_value (255)
                                                                                # threshold is basically the threshold you set (150)
                                                                                # thresh is the binarized image returned
    cv.imshow("Binarized Image", thresh)

    threshold_inv, thresh_inv = cv.threshold(grey_image, 150, 255, cv.THRESH_BINARY_INV)

    cv.imshow("Inversed Binary Image", thresh_inv)


    # Adaptice Thresholding
    # A downside of Simple Thresholding is that we have to set the value of threshold manually which might not really work in binarization of an image
    # A good way of resolving this is to let the computer itself decide what to put the threshold to

    adaptive_thresh = cv.adaptiveThreshold(grey_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3) # (source, maximum_value, method, thresholding_type, block_size, c)
                                                                                                                # The meathod of thresholding is basically how computer handles the calculation of finding threshold (here is mean)
                                                                                                                # Type of thresholding is the same as Simple Thresholding
                                                                                                                # block_size basically tells how far do we let the pixels to affect the mean method
                                                                                                                # c is just a parameter letting us to fine-tune our thresholder
    cv.imshow("Adaptive Threshold", adaptive_thresh) 

    # There are different methods of computing thresholds e.g. Gaussian, which adds wrights to pixels
    # In order to find what is best we have to really hand tune the parameters and methods to get the best results


    cv.waitKey(0)
    cv.destroyAllWindows()




if __name__ == "__main__":
    main()