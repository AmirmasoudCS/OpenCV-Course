import cv2 as cv
from _04_basics.grey_scale import to_grey
from _04_basics.blur import blur
from _04_basics.edge_cascade import find_edge
from _04_basics.dilating import dilate
from _04_basics.eroding import erode


def main():

    image = cv.imread("assets/Photos/img3.jpg")

    choice = input("What do  you want to do?\n(1) Convert to grey scale\n(2) Blur the image.\n(3) Find the edges of an image.\n(4) Blur and find the edges of an image.\n(5) Dilate an image.\n(6) Eroding an image.\n")

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

    elif choice == "3":

        th1 = int(input("Please input the value for threshold1: "))
        th2 = int(input("Please input the value for threshold2: "))

        canny_image = find_edge(image, th1, th2)

        cv.imshow("Original Image", image)
        cv.imshow("Edges Found Image", canny_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif choice == "4":

        blured_image = blur(image)

        th1 = int(input("Please input the value for threshold1: "))
        th2 = int(input("Please input the value for threshold2: "))

        canny_image = find_edge(image, th1, th2)
        canny_blurred_image = find_edge(blured_image, th1, th2)

        cv.imshow("Original Image", image)
        cv.imshow("Blurred Image", blured_image)
        cv.imshow("Edges in teh Original Image", canny_image)
        cv.imshow("Edges in the Blured Image", canny_blurred_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif choice == "5":

        kernel_size: tuple[int, int] = eval(input("Please enter the kernel size in the (x, y) format: "))
        iterations = int(input("Please enter the number of iterations: "))

        canny_image = find_edge(image)
        dilated_image = dilate(canny_image, kernel_size, iterations)

        cv.imshow("Original Image", image)
        cv.imshow("Canny Image", canny_image)
        cv.imshow("Dilated Image", dilated_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif choice == "6":

        kernel_size: tuple[int, int] = eval(input("Please enter the kernel size in the (x, y) format: "))
        iterations = int(input("Please enter the number of iterations: "))

        canny_image = find_edge(image)
        dilated_image = dilate(canny_image, kernel_size, iterations)
        eroded_image = erode(dilated_image, kernel_size, iterations)

        cv.imshow("Original Image", image)
        cv.imshow("Canny Image", canny_image)
        cv.imshow("Dilated Image", dilated_image)
        cv.imshow("Eroded Image", eroded_image)
        cv.waitKey(0)
        cv.destroyAllWindows()
        
    else:
        print("Wrong input!")
        return
    

if __name__ == "__main__":
    main()