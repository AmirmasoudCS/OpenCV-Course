import cv2 as cv
import numpy as np

# 1. Paint the image a certain color
def paint_image(image):

    choice = input("waht color do you want to paint the image? (red, green, blue):\n ")

    if choice == "red":
        image[:] = [0, 0, 255]  # BGR format for red
    elif choice == "green":
        image[:] = [0, 255, 0]  # BGR format for green
    elif choice == "blue":
        image[:] = [255, 0, 0]  # BGR format for blue
    else:
        print("Invalid color choice. Please choose red, green, or blue.")
        print("Returning the original image without any changes.")
        return image

    return image

def paint_portion(image, start_x, finish_x, start_y, finish_y):
    choice = input("What color do you want to paint the portion of the image? (red, green, blue):\n ")

    if choice == "red":
        image[start_y:finish_y, start_x:finish_x] = [0, 0, 255]  # BGR format for red
    elif choice == "green":
        image[start_y:finish_y, start_x:finish_x] = [0, 255, 0]  # BGR format for green
    elif choice == "blue":
        image[start_y:finish_y, start_x:finish_x] = [255, 0, 0]  # BGR format for blue
    else:
        print("Invalid color choice. Please choose red, green, or blue.")
        print("Returning the original image without any changes.")
        return image

    return image

def draw_rectangle(image, start_x, finish_x, start_y, finish_y, color="red", thickness=-1):
    if color == "red":
        cv.rectangle(image, (start_x, start_y), (finish_x, finish_y), (0, 0, 255), thickness)
    elif color == "green":
        cv.rectangle(image, (start_x, start_y), (finish_x, finish_y), (0, 255, 0), thickness)
    elif color == "blue":
        cv.rectangle(image, (start_x, start_y), (finish_x, finish_y), (255, 0, 0), thickness)


def main():

    blank = np.zeros((500, 500, 3), dtype='uint8') # Giving in the width, height, and number of color channels (3 for RGB) and dtype = uint8 for 8-bit unsigned integers (0-255)

    choice = input("What do you want to do with the image?\n(1) Paint all the image.\n(2) Paint a protion of the image.\n(3) Draw a rectangle.\n")

    if choice == "1":
        painted_image = paint_image(blank)
        cv.imshow("Painted Image", painted_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif choice == "2":

        while True:
            start_x = int(input("Enter the starting x-coordinate of the portion to paint (0-499): "))
            if start_x < 0 or start_x > 499:
                print("Invalid starting x-coordinate. Please enter a value between 0 and 499.")
                continue
            break

        while True:
            finish_x = int(input("Enter the finishing x-coordinate of the portion to paint (0-499): "))
            if finish_x < 0 or finish_x > 499:
                print("Invalid finishing x-coordinate. Please enter a value between 0 and 499.")
                continue
            if finish_x <= start_x:
                print("Finishing x-coordinate must be greater than starting x-coordinate. Please enter a valid value.")
                continue
            break

        while True:
            start_y = int(input("Enter the starting y-coordinate of the portion to paint (0-499): "))
            if start_y < 0 or start_y > 499:
                print("Invalid starting y-coordinate. Please enter a value between 0 and 499.")
                continue
            break

        while True:
            finish_y = int(input("Enter the finishing y-coordinate of the portion to paint (0-499): "))
            if finish_y < 0 or finish_y > 499:
                print("Invalid finishing y-coordinate. Please enter a value between 0 and 499.")
                continue
            if finish_y <= start_y:
                print("Finishing y-coordinate must be greater than starting y-coordinate. Please enter a valid value.")
                continue
            break

        painted_image = paint_portion(blank, start_x, finish_x, start_y, finish_y)

        cv.imshow("Painted Portion of Image", painted_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif choice == "3":
        while True:
            start_x = int(input("Enter the starting x-coordinate of the rectangle (0-499): "))
            if start_x < 0 or start_x > 499:
                print("Invalid starting x-coordinate. Please enter a value between 0 and 499.")
                continue
            break

        while True:
            finish_x = int(input("Enter the finishing x-coordinate of the rectangle (0-499): "))
            if finish_x < 0 or finish_x > 499:
                print("Invalid finishing x-coordinate. Please enter a value between 0 and 499.")
                continue
            if finish_x <= start_x:
                print("Finishing x-coordinate must be greater than starting x-coordinate. Please enter a valid value.")
                continue
            break

        while True:
            start_y = int(input("Enter the starting y-coordinate of the rectangle (0-499): "))
            if start_y < 0 or start_y > 499:
                print("Invalid starting y-coordinate. Please enter a value between 0 and 499.")
                continue
            break

        while True:
            finish_y = int(input("Enter the finishing y-coordinate of the rectangle (0-499): "))
            if finish_y < 0 or finish_y > 499:
                print("Invalid finishing y-coordinate. Please enter a value between 0 and 499.")
                continue
            if finish_y <= start_y:
                print("Finishing y-coordinate must be greater than starting y-coordinate. Please enter a valid value.")
                continue
            break

        color = input("What color do you want the rectangle to be? (red, green, blue):\n ")
        if color not in ["red", "green", "blue"]:
            print("Invalid color choice. Initiating with default color red.")
            color = "red"

        thickness = int(input("Enter the thickness of the rectangle border (positive integer, or -1 for filled): "))
        if thickness < -1:
            print("Invalid thickness. Initiating with default thickness -1 (filled).")
            thickness = -1

        draw_rectangle(blank, start_x, finish_x,  start_y, finish_y, color, thickness)


if __name__ == "__main__":
    main()