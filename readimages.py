#!/usr/bin/python3

import numpy as np
import sys
import cv2

IMAGE_PATH = "/tmp/images/"
IMAGE_FILENAME = "neon_dark"

def main():
    print(3)
    img = cv2.imread(IMAGE_PATH + IMAGE_FILENAME,  0)
    print(img.shape)
    cv2.imshow('image',img)
    cv2.waitKey(1)
    cv2.destroyAllWindows()

if(__name__ == '__main__'):
    main()