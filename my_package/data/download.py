from PIL import Image
import requests
from io import BytesIO
import json
import os


class Download(object):
    '''
        A class for helping in dowloading the required images from the given url to the specified path
    '''

    def __call__(self, path, url):

        self.path = path

        r = requests.get(url).content
        with open(f"{path}", "wb+") as f:
            f.write(r)

        '''
            Arguments:
            path: download path with the file name
            url: required image URL
        '''


path = r'C:\Users\irnma\OneDrive\Desktop\Ritesaah\CS29006_SW_Lab_Spr2023\Python_DS_Assignment_Question_02\data\imgs\0.jpg'
url = 'http://farm5.staticflickr.com/4127/5172389204_31214fdc50_z.jpg'
d = Download()
d.__call__(path, url)
