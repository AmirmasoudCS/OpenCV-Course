import cv2 as cv
import numpy as np


def main():

    image = cv.imread("assets/Photos/img3.jpg")

    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


    # Laplacian
    
    lap = cv.Laplacian(grey_image, cv.CV_64F)
    lap = np.uint8(np.absolute(lap))

    cv.imshow("Laplacian Image", lap)





    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()