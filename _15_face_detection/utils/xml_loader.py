import cv2 as cv
from pathlib import Path

def load_xml(path:Path):

    return cv.CascadeClassifier(path)