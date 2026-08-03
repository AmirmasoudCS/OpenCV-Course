import cv2 as cv
import numpy as np


def main():

    image = cv.imread("assets/Photos/img3.jpg")

    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


    # Laplacian
    # Computes the Gradiants of the image passed to it
    # Converting black to white and white to black are considered the negative and possitive slopes of the Gradiant and since images themselves can not contain negative pixels
    # so we compute the absolute ( |pixel_value | ) of pixels values and convert them to uint8 

    lap = cv.Laplacian(grey_image, cv.CV_64F)
    lap = np.uint8(np.absolute(lap))

    cv.imshow("Laplacian Image", lap)


    # Sobel
    # Computes Gradiants in two directions: (1) x-axis (2) y-axis
    
    sobelx = cv.Sobel(grey_image, cv.CV_64F, 1, 0)  # 1 : x-axis, 0 : y-axis
    sobely = cv.Sobel(grey_image, cv.CV_64F, 0, 1)  # 0: x-axis, 1 : y-axis
    combined_sobel = cv.bitwise_or(sobelx, sobely)

    cv.imshow("Sobel X", sobelx)
    cv.imshow("Sobel Y", sobely)
    cv.imshow("Combined Sobel", combined_sobel)

    # Canny

    canny = cv.Canny(grey_image, 150, 175)

    cv.imshow("Canny Image", canny)




    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()