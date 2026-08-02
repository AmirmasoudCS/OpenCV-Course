import cv2 as cv

def main():

    image = cv.imread("assets/Photos/img6.jpg")
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
    

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()