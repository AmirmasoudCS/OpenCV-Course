#   ____________
#   |___|___|___|   These are the pixels of a place in the image when we have selected a kernel size of (3, 3)
#   |___|___|___|   and what happens is that by the method of bluring that we have selected (e.g. Averaging), something
#   |___|___|___|   happens to the pixel in the middle, by the pixels around it (also called surrounding pixels)
#   

import cv2 as cv

def main():

    image = cv.imread("assets/Photos/boston_park.jpg")
    cv.imshow("Original Image", image)

    # Averaging
    # In this method, the middle pixel is the average of pixel intensity of the surronding pixels of it

    average = cv.blur(image, (3, 3))
    cv.imshow("Average Blur", average)

    # Gaussian
    # Instead of computing the average, each surrounding pixel is given a particular wright and the weighted average gives the true result for the center
    # In the Gaussian method the image tends to get less blur, but it is more natural

    gaussian = cv.GaussianBlur(image, (3, 3), 0) # 0 is the standard deviation in the x-axis
    cv.imshow("Gaussian Blur", gaussian) 

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()