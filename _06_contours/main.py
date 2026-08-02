# Contours are basically the boundaries of objects, the line that occurs that joint the continuous points along the boundary of an object
# From a mathematical view they are not the same as the edges ( you can get away mostly with contours=edges )
import cv2 as cv
from _04_basics.grey_scale import to_grey
from _04_basics.edge_cascade import find_edge
from _04_basics.blur import blur
from _06_contours.find_contours import find_contours
from _06_contours.threshold import threshold

def main():

    img = cv.imread("assets/Photos/eiffel_tower_2.jpg")
    grey_img = to_grey(img)

    choice = int(input("Which method of finding contours you want to do?\n(1) Blurring --> canny --> contours.\n(2) cv.threshold().\n"))

    if choice == 1:

        blurred_image = blur(grey_img)
        canny_image = find_edge(blurred_image, th1=125, th2=175)
        contours, hierarchies = find_contours(canny_image)

        print(f"{len(contours)} contour(s) were found!")

        cv.imshow("Canny Image", canny_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif choice == 2:
        threshold_value = int(input("Please enter the threshold value: "))
        maximum_value = int(input("Please enter the maximum value: "))

        ret, thresh = threshold(img=grey_img, threshold=threshold_value, maximum=maximum_value)

        contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

        print(f"{len(contours)} contour(s) were found!")

        cv.imshow("Thresh", thresh)
        cv.waitKey(0)
        cv.destroyAllWindows()


    else:
        print("Wrong input!")
        return
    


if __name__ == "__main__":
    main()