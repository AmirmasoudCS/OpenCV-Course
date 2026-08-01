import cv2 as cv
from _04_basics.grey_scale import to_grey

def main():

    image = cv.imread("assets/Photos/img4.jpg")

    choice = "What do  you want to do?\n(1) Convert to grey scale\n"

    if choice == "1":
        
        grey_image = to_grey(image)

        cv.imshow("Original Image", image)
        cv.imshow("Grey Image", grey_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

if __name__ == "__main__":
    main()