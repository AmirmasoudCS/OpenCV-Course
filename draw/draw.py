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

    return image

def main():

    blank = np.zeros((500, 500), dtype='uint8')

    choice = input("What do you want to do with the image?\n (1) Paint the image.")

    if choice == "1":
        painted_image = paint_image(blank)
        cv.imshow("Painted Image", painted_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

if __name__ == "__main__":
    main()