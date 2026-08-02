import cv2 as cv
from _05_transformations.translation import translate

def main():

    image = cv.imread("assets/Photos/img2.jpg")

    choice = input("Waht you want to do?\n(1) Translate and image.\n")

    if choice == "1":
        x = input("Please input x: ")
        y = input("please input y: ")

        translated_image = translate(image, x, y)

        cv.imshow("Original Image", image)
        cv.imshow("Translated Image", translated_image)
        cv.waitKey(0)
        cv.destroyAllWindows()


    else:
        print("Invalid input of an option!")
        return



if __name__ == "__main__":
    main()