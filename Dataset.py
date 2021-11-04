import glob
import os
import numpy as np
import cv2

class Dataset():

    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.classes = [os.path.basename(dir) for dir in glob.glob(self.data_dir+"/*")]
        self.length = sum(self.__imageCount().values())
        self.lengths_by_class = self.__imageCount()
        self.shape = tuple((self.length, *self.__shape()))
        self = self.__take_data()
        
        
    def __imageCount(self):
        """
        Returns sum of .png, .jpg, .jpeg file counts.
        """
        images = dict()
        for subdir in self.classes:
            images[subdir] = 0
            images[subdir] += len(glob.glob(self.data_dir + "/" +subdir +"/*.png"))
            images[subdir] += len(glob.glob(self.data_dir + "/" +subdir +"/*.jpg"))
            images[subdir] += len(glob.glob(self.data_dir + "/" +subdir +"/*.jpeg"))
        return images
    
    def __take_data(self):  
        image_pool = np.array([])
        for subdir in self.classes:
            print("Class "+subdir+"'s objects are creating.")
            for i,path in enumerate(glob.glob(self.data_dir + "/" +subdir +"/*.png") + \
                                    glob.glob(self.data_dir + "/" +subdir +"/*.jpg") + \
                                    glob.glob(self.data_dir + "/" +subdir +"/*.jpeg")):
                image = cv2.imread(path)
                image_pool = np.append(image_pool, image).reshape(-1,image.shape[0],image.shape[1],image.shape[2])
                print(f"{subdir}: {(i/self.lengths_by_class[subdir])*100}")
        print("*"*25)
        return image_pool

    def __getitem__(self, item):
         return getattr(self, item)

    def __shape(self):
        for subdir in self.classes:
            for path in glob.glob(self.data_dir + "/" +subdir +"/*.png") + \
                        glob.glob(self.data_dir + "/" +subdir +"/*.jpg") + \
                        glob.glob(self.data_dir + "/" +subdir +"/*.jpeg"):
                image = cv2.imread(path)
                return image.shape
    
