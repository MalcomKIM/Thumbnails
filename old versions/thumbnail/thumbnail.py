# -*- coding: utf-8 -*-
"""
Created on Sun May 31 09:57:49 2020

@author: Malcolm
"""

from PIL import Image
from os import listdir
import math
import sys

def getfolderName():
    # get folder name from cmd
    try:
        folder_name=sys.argv[1]
        folder_name=folder_name+"/"
    except:
        print('Please pass folder name')
        
    return folder_name

def loadImages(path):
    # return array of images
    try:
        imagesList = listdir(path)
    except:
        print('Please pass a correct folder name')
        return
    
    loadedImages = []
    for image in imagesList:
        img = Image.open(path + image)
        loadedImages.append(img)

    return loadedImages

def generate_thumbnail(images):
    element_size=(256,256)
    container_size=(300,300)
    
    columns=(math.ceil(math.sqrt(len(images))))
    
    masterWidth = container_size[0] * columns
    masterHeight = container_size[1] * int(math.ceil(len(images) / columns))
    
    finalImage = Image.new('RGB', size=(masterWidth, masterHeight),color = (255, 255, 255))
    
    row=0
    col=0
    
    for im in images:
        im.thumbnail(element_size)
        locationX = container_size[0] * col + int((container_size[0] - element_size[0])/2)
        locationY = container_size[1] * row
    
        finalImage.paste(im, (locationX, locationY))
        col += 1
        
        if col == columns:
            row += 1
            col = 0
        
    return finalImage

if __name__ == "__main__":
    images = loadImages(getfolderName())
    
    thumbnail=generate_thumbnail(images)
    thumbnail.show()
    thumbnail.save("thumbnail.jpg")
