import cv2 as cv

def main():

    image = cv.imread("assets/Photos/img6.jpg")
    cv.imshow("Original Image", image)

    # BGR to Greyscale

    grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    cv.imshow("Grey Image", grey)

    # Greyscale images show you the distribution of the pixel intensities at particulatr palces of your image

    # BGR to HSV (based on how humans think and can see the color)

    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    cv.imshow("HSV Image", hsv)

if __name__ == "__main__":
    main()