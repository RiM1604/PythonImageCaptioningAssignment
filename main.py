#Imports
from my_package.model import ImageCaptioningModel
# from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import numpy as np
import jsonlines
import os 
from PIL import Image 
# Image.MAX_IMAGE_PIXELS = 1000000000000
# os.environ["CURL_CA_BUNDLE"]=""
from PIL import Image
from my_package.model import ImageCaptioningModel
from my_package.data.dataset import Dataset
from my_package.data.download import Download
from my_package.data.transforms.blur import BlurImage
from my_package.data.transforms.crop import CropImage, RandomCrop
from my_package.data.transforms.flip import FlipImage
from my_package.data.transforms.rescale import RescaleImage
from my_package.data.transforms.rotate import RotateImage

counter=1

def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    '''
    global counter
    if os.path.exists('data\imgs\transformedimgs')==None:
        os.mkdir('data\imgs\transformedimgs')
  
    #Create the instances of the dataset, download

    annotationpath=annotation_file
    f=jsonlines.open(annotationpath)
    f=list(f)
    

    
    #Print image names and their captions from annotation file using dataset object
    d=Dataset(annotationpath)
    for i in range(d.__len__()):
        obj=d.__getann__(i)
        name=obj['file_name']
        captions=obj['captions'] 
        print('name is '+name)
        print('captions are:')
        for i in range(len(captions)):
            key=captions[i]
            value=key['caption']
            print(value)      
        print('\n')

    #Download images to ./data/imgs/ folder using download object
    for i in range(len(f)):
        dict=f[i]
        link=dict['url']
        filename=dict['file_name']
        storagepath='data\imgs'
        path=storagepath+f'\{filename}'
        d=Download()
        d.__call__(path,link)


    #Transform the required image (roll number mod 10) and save it seperately

    d1=Dataset(annotationpath,transforms)
    imageobj=f[1]
    
    name=imageobj['file_name']
    requrl=storagepath+f'\{name}'
    transimage=d1.__transformitem__(requrl)
    savepath=outputs+f'/{counter}.jpg'
    transimage.save(savepath)
    p=captioner(outputs+f'/{counter}.jpg',3)
    for i in range(len(p)):
        print(p[i])
        print('\n')
    counter=counter+1
    
    #Get the predictions from the captioner for the above saved transformed image  


def main():
    captioner = ImageCaptioningModel()
    experiment(r'./data/annotations.jsonl', captioner, None, 'data/imgs/transformedimgs') # Sample arguments to call experiment()
    experiment(r'./data/annotations.jsonl', captioner, [FlipImage()], 'data/imgs/transformedimgs') # Sample arguments to call experiment()
    experiment(r'./data/annotations.jsonl', captioner, [BlurImage(5)], 'data/imgs/transformedimgs')
    experiment(r'./data/annotations.jsonl', captioner, [RescaleImage(2)], 'data/imgs/transformedimgs')
    experiment(r'./data/annotations.jsonl', captioner, [RescaleImage(0.5)], 'data/imgs/transformedimgs')
    experiment(r'./data/annotations.jsonl', captioner, [RotateImage(90), BlurImage(1)], 'data/imgs/transformedimgs')
    experiment(r'./data/annotations.jsonl', captioner, [RotateImage(45), BlurImage(1)], 'data/imgs/transformedimgs')
    #experiment(r'./data/annotations.jsonl', captioner, [RandomCrop((100,100)), BlurImage(1)], 'data/imgs/transformedimgs')

    




if __name__ == '__main__':
    main()