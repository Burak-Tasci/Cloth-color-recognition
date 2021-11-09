import glob
import os
import cv2

class Dataset:

    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.classes = [os.path.basename(dir) for dir in glob.glob(self.data_dir+"\\*")]
        self.length = sum(self.__imageCount().values())
        self.lengths_by_class = self.__imageCount()
        self.shape = tuple((self.length,*self.__shape()))
        self.images, self.labels, self.paths = self.__create_images_and_labels()

    def __imageCount(self):
        """
        Returns sum of .png, .jpg, .jpeg file counts.
        """
        images = dict()
        for subdir in self.classes:
            images[subdir] = 0
            images[subdir] += len(glob.glob(self.data_dir + "\\" +subdir +"\\*.png"))
            images[subdir] += len(glob.glob(self.data_dir + "\\" +subdir +"\\*.jpg"))
            images[subdir] += len(glob.glob(self.data_dir + "\\" +subdir +"\\*.jpeg"))
        return images
    
    def __create_images_and_labels(self):  
        """
        Creates images from paths, creates labels from paths.
        Returns images and labels as separate arrays.
        """
        image_paths = []
        image_pool = []
        label_pool = []
        for subdir in self.classes:
            print("Class "+subdir+"'s objects are creating.")
            for i,path in enumerate(glob.glob(self.data_dir + "\\" +subdir +"\\*.png") + \
                                    glob.glob(self.data_dir + "\\" +subdir +"\\*.jpg") + \
                                    glob.glob(self.data_dir + "\\" +subdir +"\\*.jpeg")):

                image = cv2.imread(path)
                image_pool.append(image)
                label_pool.append(subdir)
                image_paths.append(path)
                print(f"{subdir}: {(i/self.lengths_by_class[subdir])*100:.4}",end="\r")
            print("Class "+subdir+" objects creation has done.")
        print("Completed!")
        return image_pool, label_pool, image_paths

    def __shape(self):
        for subdir in self.classes:
            for path in glob.glob(self.data_dir + "\\" +subdir +"\\*.png") + \
                        glob.glob(self.data_dir + "\\" +subdir +"\\*.jpg") + \
                        glob.glob(self.data_dir + "\\" +subdir +"\\*.jpeg"):
                image = cv2.imread(path)
                return image.shape
    
