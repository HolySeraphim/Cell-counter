import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib
from cvlib.object_detection import draw_bbox

image = cv2.imread("tryphoto/New/Fluorescent-E.-coli.tif")
box, label, count = cvlib.detect_common_objects(image)
output = draw_bbox(image, box, label, count)
print(label)
print(f"Количество объектов на картинке: {label.count('person')}")
 
plt.imshow(output)
plt.show()
print(image)