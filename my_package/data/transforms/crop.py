#Imports
from PIL import Image
import random
import time

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        self.shape=shape
        self.type=crop_type
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''

    def __call__(self, image):
       
        if self.type=='center':
            frac=(self.shape[0]*self.shape[1])/(image.size[0]*image.size[1])
            left=image.size[0]*((1-frac)/2)
            upper=image.size[1]*((1-frac)/2)
            right=image.size[0]-((1-frac)/2)*image.size[0]
            bottom=image.size[1]-((1-frac)/2)*image.size[1]
            croppedimage=image.crop((left,upper,right,bottom))
            return croppedimage

        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image        '''
class RandomCrop(object):
        def __init__(self,shape):
            self.shape=shape
        def __call__(self,image):
            random.seed=time.time()
            x=random.randint(0,image.size[0]-self.shape[0])
            y=random.randint(0,image.size[1]-self.shape[1])
            croppedimage=image.crop((x,y,x+self.shape[0],y+self.shape[1]))
            return croppedimage
            




