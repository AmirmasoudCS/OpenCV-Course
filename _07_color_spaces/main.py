import cv2 as cv

def main():

    image = cv.imread("assets/Photos/img6.jpg")
    cv.imshow("Original Image", image)

    # BGR to Greyscale

    grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    cv.imshow("Grey Image", grey)

    

if __name__ == "__main__":
    main()