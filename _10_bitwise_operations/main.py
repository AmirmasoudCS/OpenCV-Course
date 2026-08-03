# There are four bitwise operators: AND, OR, XOR, NOT
# These operators are used alot in image processing (specially with masks)
# They operator in a binary matter, a pixel i turned off with the value 0, and it is turned on with the value 1

import cv2 as cv
import numpy as np

def main():

    blank = np.zeros((400, 400), dtype="uint8")

    rectangle = cv.rectangle(blank.copy(), (30, 30), (370,370), 255, -1) # Since the image is represented in binary we don't have to give the color in BGR format and we can ust give one value (255 here)

    circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

    cv.imshow("Rectangle", rectangle)
    cv.imshow("Circle", circle)


    # Bitwise AND

    bitwise_and = cv.bitwise_and(rectangle, circle)
    cv.imshow("AND", bitwise_and)

    # Bitwise OR

    bitwise_or = cv.bitwise_or(rectangle, circle)
    cv.imshow("OR", bitwise_or)

    # Bitwise XOR

    bitwise_xor = cv.bitwise_xor(rectangle, circle)
    cv.imshow("XOR", bitwise_xor)

    # Bitwise NOT

    rectangle_not = cv.bitwise_not(rectangle)
    circle_not = cv.bitwise_not(circle)

    cv.imshow("Rectangle NOT", rectangle_not)
    cv.imshow("Circle NOT", circle_not)
    cv.imshow("NOT Circle ^ NOT Rectangle", cv.bitwise_and(rectangle_not, circle_not))


    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()