#Imports
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self.size=output_size

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        if type(self.size)==tuple:
            im=image.resize(self.size)
        else:
            height=image.height
            width=image.width
            nheight=height*self.size
            nwidth=width*self.size
            new_size=(int(nwidth),int(nheight))
            im=image.resize(new_size)
        
        return im


