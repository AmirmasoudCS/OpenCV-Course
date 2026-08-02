import cv2 as cv
import matplotlib.pyplot as plt

def main():

    image = cv.imread("assets/Photos/img5.jpg")
    cv.imshow("Original Image", image)

    # BGR to Greyscale

    grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    cv.imshow("Grey Image", grey)

    # Greyscale images show you the distribution of the pixel intensities at particulatr palces of your image

    # BGR to HSV 

    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    cv.imshow("HSV Image", hsv)

    # Based on how humans think and can see the color

    # BGR to LAB or L*a*b

    lab = cv.cvtColor(image, cv.COLOR_BGR2LAB)

    cv.imshow("LAB", lab)

    #

    # Since OpenCV library reads images in BGR color space, if you want to show an image that was read by cv, with another library (like matplotlib), you get exactly the inversion of the colors

    plt.imshow(image)
    plt.show()

    # 

    # BGR to RGB

    rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    cv.imshow("RGB", rgb)
    plt.imshow(rgb)
    plt.show()

    cv.waitKey(0)
    cv.destroyAllWindows()


    # You can do the inverse of whatever you did now e.g.
    # Greyscale --> BGR
    # HSV --> BGR ...
    # But you can not directly convert something like Greyscale --> HSV (X)
    # Inorder to do that you need to Greyscale --> BGR --> HSV

if __name__ == "__main__":
    main()