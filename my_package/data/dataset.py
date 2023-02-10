# Imports
import jsonlines
from PIL import Image
import os
import numpy as np


class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.transforms = transforms
        self.annpath = annotation_file
        f = jsonlines.open(f'{self.annpath}')
        self.obj = f
        self.listobj = list(f)

    def __len__(self):
        length = len(self.listobj)
        return length
        '''
            return the number of data points in the dataset
        '''

    def __getann__(self, idx):
        self.index = idx
        d = self.listobj
        return d[self.index]

        '''
            return the data items for the index idx as an object
        '''

    def __transformitem__(self, path):

        self.timage = Image.open(path)
        if self.transforms != None:
            for i in range(len(self.transforms)):
                self.timage = self.transforms[i].__call__(self.timage)
            return self.timage
        elif self.transforms == None:
            return self.timage
        '''
            return transformed PIL Image object for the image in the given path
        '''

# d=Dataset('./data/annotations.jsonl',[FlipImage(), BlurImage(1)])
# d.__transformitem__(r'C:\Users\irnma\OneDrive\Desktop\Ritesaah\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\1.jpg')
