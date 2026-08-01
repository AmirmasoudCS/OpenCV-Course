import cv2 as cv
from _04_basics.grey_scale import to_grey
from _04_basics.blur import blur

def main():

    image = cv.imread("assets/Photos/img4.jpg")

    choice = input("What do  you want to do?\n(1) Convert to grey scale\n(2) Blur the image.\n")

    if choice == "1":
        
        grey_image = to_grey(image)

        cv.imshow("Original Image", image)
        cv.imshow("Grey Image", grey_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif choice == "2":

        blured_image = blur(image)

        cv.imshow("Original Image", image)
        cv.imshow("Blurred Image", blured_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    else:
        print("Wrong input!")
        return
    

if __name__ == "__main__":
    main()