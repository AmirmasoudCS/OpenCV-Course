import cv2 as cv
from _05_transformations.translation import translate
from _05_transformations.rotation import rotate

def main():

    image = cv.imread("assets/Photos/img2.jpg")

    choice = input("Waht you want to do?\n(1) Translate an image.\n(2) Rotate an image.\n")

    if choice == "1":
        x = input("Please input x: ")
        y = input("please input y: ")

        translated_image = translate(image, x, y)

        cv.imshow("Original Image", image)
        cv.imshow("Translated Image", translated_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif choice ==" 3":

        angle = int(input("please enter the angle you wish to rotate the image with: "))
        angle = angle % 360

        rotation_center: tuple[int, int] = eval(input("Please enter the rotation point in the form of (x, y): "))

        rotated_image = rotate(image, angle, rotation_center)

        cv.imshow("Original Image", image)
        cv.imshow("Rotated Image", rotated_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    else:
        print("Invalid input of an option!")
        return



if __name__ == "__main__":
    main()