from Dataset import Dataset
import cv2
import numpy as np

dataset = Dataset("./data/")
print(dataset.classes)
print(dataset.length)
print()
print(dataset.shape)

img = dataset[0]

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



