import itertools
from Dataset import Dataset
import matplotlib.pyplot as plt
import cv2
import numpy as np
import pandas as pd

# Colors data file
class ColorRecogniser:
    """docstring for Color"""
    def __init__(self, colors_csv="./colors.csv"):
        super(ColorRecogniser, self).__init__()
        index=["color","color_name","hex","B","G","R"]
        self.colors_data = pd.read_csv(colors_csv, names = index, header = None)
        
    def getColorName(self,R,G,B):
        # including colors_csv
        # minimum variable for finding the closest color
        minimum = 1000
        # testing colors one by one
        for i in range(len(self.colors_data)):
            d = abs(R- int(self.colors_data.loc[i,"B"])) + abs(G- int(self.colors_data.loc[i,"G"]))+ abs(B- int(self.colors_data.loc[i,"R"]))
            if(d<minimum):
                minimum = d
                color_name = self.colors_data.loc[i,"color_name"]
        return color_name

    def getColors(self,img):
        pixels = np.float32(img.reshape(-1, 3))
        n_colors = 2
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
        flags = cv2.KMEANS_RANDOM_CENTERS
        _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
        _, counts = np.unique(labels, return_counts=True)

        return palette



