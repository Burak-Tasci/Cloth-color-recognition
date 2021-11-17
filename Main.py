import cv2
import pandas as pd
from Color import ColorRecogniser
import argparse
import numpy as np
import matplotlib.pyplot as plt

# Returns synced  color
def getSyncColor(image_colors,bg_colors):
    for im in image_colors:
        for bg in bg_colors:
            if im == bg:
                return im

# Returns diff between image_colors and synced color
def diff(sync_color, image_colors):
    for i in image_colors:
        if i != sync_color:
            return i


# Argument Parser for CLI
ap = argparse.ArgumentParser()
ap.add_argument("--image", "-i", required=True,
								help="Image")
ap.add_argument("--colors", "-c", required=True,
								help="Colors csv file")
args = vars(ap.parse_args())

# Image's Colors
ImagesAndColors = pd.read_csv(args["colors"])
Colors = ImagesAndColors["Name"]

# Taking borders and image
img = cv2.imread(args["image"])
cv2.imshow("img",img)
top_border = img[:1,:]
left_border = img[:,:1]
right_border = img[:,-2:-1]

image_colors = []
bg_colors = []


recogniser = ColorRecogniser(args["colors"])

# LEFT BORDER
dominants = recogniser.getColors(left_border)
b,g,r = dominants[0]
bg_colors.append(recogniser.getColorName(b,g,r))
b,g,r = dominants[1]
bg_colors.append(recogniser.getColorName(b,g,r))

# RIGHT BORDER
dominants = recogniser.getColors(right_border)
b,g,r = dominants[0]
bg_colors.append(recogniser.getColorName(b,g,r))
b,g,r = dominants[1]
bg_colors.append(recogniser.getColorName(b,g,r))

# TOP BORDER
dominants = recogniser.getColors(top_border)
b,g,r = dominants[0]
bg_colors.append(recogniser.getColorName(b,g,r))
b,g,r = dominants[1]
bg_colors.append(recogniser.getColorName(b,g,r))


# IMAGE
dominants = recogniser.getColors(img)
b,g,r = dominants[0]
image_colors.append(recogniser.getColorName(b,g,r))
b,g,r = dominants[1]
image_colors.append(recogniser.getColorName(b,g,r))

# printing synced color
bg = getSyncColor(image_colors, bg_colors)
cloth_color = diff(bg,image_colors)
print("Cloth color:",cloth_color)

##### PLOTTING

color_df = ImagesAndColors[ImagesAndColors["Name"] == cloth_color]
rgb = color_df.loc[:,["Red (8 bit)","Green (8 bit)","Blue (8 bit)"]]

color = np.ones([256,256,3], dtype=np.uint8) * rgb.loc[:,["Red (8 bit)","Green (8 bit)","Blue (8 bit)"]].values
plt.title("CLOTHE COLOR")
plt.xticks([])
plt.yticks([])
plt.imshow(color)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

