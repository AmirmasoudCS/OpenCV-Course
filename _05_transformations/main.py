import cv2 as cv
from _05_transformations.translation import translate
from _05_transformations.rotation import rotate
from _05_transformations.flip import flip

def main():

    image = cv.imread("assets/Photos/img2.jpg")

    choice = input("Waht you want to do?\n(1) Translate an image.\n(2) Rotate an image.\n(3) Flip an image.\n")

    if choice == "1":
        x = input("Please input x: ")
        y = input("please input y: ")

        translated_image = translate(image, x, y)

        cv.imshow("Original Image", image)
        cv.imshow("Translated Image", translated_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif choice == "2":

        angle = int(input("please enter the angle you wish to rotate the image with: "))
        angle = angle % 360

        rotation_center: tuple[int, int] = eval(input("Please enter the rotation point in the form of (x, y) (-1 for default): "))

        rotated_image = rotate(image=image, angle=angle, rotation_point=rotation_center if rotation_center is not -1 else None)

        cv.imshow("Original Image", image)
        cv.imshow("Rotated Image", rotated_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif choice == "3":

        flip_choice = int(input("What axis do you want to flip against? (0:x, 1:y, -1:both)"))

        if choice not in (1,-1,0):
            print("Wrong choice!")
            return

        flipped_image = flip(image, flip_choice)

        cv.imshow("Original Image", image)
        cv.imshow("Flipped Image", flipped_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    else:
        print("Invalid input of an option!")
        return



if __name__ == "__main__":
    main()