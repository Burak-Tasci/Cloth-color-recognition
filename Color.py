from matplotlib import colors
from Dataset import Dataset
import matplotlib.pyplot as plt
import cv2
import numpy as np
import pandas as pd

colors_csv = None

def getColorName(R,G,B):
    global colors_csv
    minimum = 1000
    for i in range(len(colors_csv)):
        d = abs(R- int(colors_csv.loc[i,"R"])) + abs(G- int(colors_csv.loc[i,"G"]))+ abs(B- int(colors_csv.loc[i,"B"]))
        if(d<minimum):
            minimum = d
            color_name = colors_csv.loc[i,"color_name"]
    return color_name

def getDominantColor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, im_bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    dilation = cv2.dilate(im_bw,(3,3),iterations = 1)
    masked_img = cv2.bitwise_and(img,img,mask = dilation)
    
    pixels = np.float32(masked_img.reshape(-1, 3))
    n_colors = 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)
    dominant = palette[np.argmax(counts)]
    return dominant

def main():
    global colors_csv
    data = Dataset("./test_data/")
    images, labels = data.images, data.labels
    # temporary img
    img = images[0]


    index=["color","color_name","hex","R","G","B"]
    colors_csv = pd.read_csv('./colors.csv', names=index, header=None)

    dominant =  getDominantColor(img)



    dominant_color = np.ones(img.shape, dtype=np.uint8) * np.uint8(dominant)
    plt.imshow(dominant_color)
    plt.show()

    r,g,b = dominant
    color_name = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)

    print(color_name)

if __name__ == "__main__":
    main()