import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib
from cvlib.object_detection import draw_bbox

image = cv2.imread("C:/Users/palpa/Desktop/Death/MIPT/ICT/Algorithms_bioinformatics/Cell_counter/tryphoto/cup.jpg")
box, label, count = cvlib.detect_common_objects(image)
output = draw_bbox(image, box, label, count)
print(label)
print(f"Количество объектов на картинке: {label.count('people')}")

plt.imshow(output)
plt.show()
print(image)