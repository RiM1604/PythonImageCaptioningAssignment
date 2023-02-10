#Imports
from PIL import Image, ImageFilter

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius):
        self.radius=radius
        
        '''
            Arguments:
            radius (int): radius to blur
        '''
  

    def __call__(self, image):
        blurimage=image.filter(ImageFilter.GaussianBlur(radius=self.radius))
        return blurimage
        
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''
