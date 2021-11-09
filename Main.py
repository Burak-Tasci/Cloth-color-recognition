import cv2
import numpy as np
from Color import ColorRecogniser
from Dataset import Dataset
from random import sample

recogniser = ColorRecogniser(".\\COLORS.csv")
dataset = Dataset(".\\test_data\\")
images = dataset.images

for i,img in enumerate(sample(images,5)):

	dominants = recogniser.getColors(img)
	
	b1,g1,r1 = dominants[0]
	b2,g2,r2 = dominants[1]

	color1 = recogniser.getColorName(b1,g1,r1)
	color2 = recogniser.getColorName(b2,g2,r2)
	print("-"*25)
	print(color1)
	print(color2)
	print("-"*25)
	cv2.imshow("img",img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	if i > 5:
		break



