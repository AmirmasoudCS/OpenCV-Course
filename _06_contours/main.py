# Contours are basically the boundaries of objects, the line that occurs that joint the continuous points along the boundary of an object
# From a mathematical view they are not the same as the edges ( you can get away mostly with contours=edges )
import cv2 as cv
from _04_basics.grey_scale import to_grey
from _04_basics.edge_cascade import find_edge
from _04_basics.blur import blur
from _06_contours.find_contours import find_contours

def main():
     
    img = cv.imread("assets/Photos/eiffel_tower_2.jpg")
    grey_img = to_grey(img)
    blurred_image = blur(grey_img)
    canny_image = find_edge(blurred_image, th1=125, th2=175)
    contours, hierarchies = find_contours(canny_image)

    print(f"{len(contours)} contour(s) were found!")

    cv.imshow("Canny Image", canny_image)
    cv.waitKey(0)
    cv.destroyAllWindows()




if __name__ == "__main__":
    main()