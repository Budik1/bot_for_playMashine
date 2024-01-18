import cv2
import numpy as np

image_file = "img/68xp.png"
img = cv2.imread(image_file)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

