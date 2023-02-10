#Imports
from PIL import Image,ImageOps

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        self.fliptype=flip_type
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''

    def __call__(self, image):
        if self.fliptype=='horizontal':
            hflip=ImageOps.mirror(image)
            return hflip
        else :
            hflip=ImageOps.flip(image)
            return hflip
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
