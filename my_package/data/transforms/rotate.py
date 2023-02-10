#Imports
from PIL import Image

class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        self.angle=degrees
        '''
            Arguments:
            degrees: rotation degree.
        '''

    def __call__(self, sample):
        rimg=sample.rotate(self.angle)
        return rimg
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

