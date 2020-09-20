# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:04:08 2020

@author: Malcom
"""

import dominate
from dominate.tags import *
from PIL import Image
import requests
from io import BytesIO
import math
import webbrowser

def readURLs():
    img_urls = []
    file = open('urls.txt', 'r')
    lines = file.readlines()

    for line in lines:
        if line[-1] == '\n':
            img_urls.append(line[:-1])
        else:
            img_urls.append(line)

    return img_urls

def loadImages(img_urls):
    # return array of images
    loadedImages = []
    for url in img_urls:
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            loadedImages.append(img)
        except:
            continue

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

def generate_html(img_urls):
    doc = dominate.document(title='Image Thumbnails')
    
    with doc.head:
        style("""
        *{
            margin: 0;
            padding: 0;
        }
        .box{
            display: flex;
            flex-wrap: wrap;
        }
        .box:after{
            content: '';
            flex-grow: 99999;
    	}
    	.imgBox{
                flex-grow: 1;
                margin: 5px;
    	}
    	.imgBox img{
    	    width: auto;
    	    height: 200px;
    	    object-fit: cover; 
    	}
        figure {
            width: -webkit-min-content;
            width: -moz-min-content;
            width: min-content;
        }
        figure.item {
            vertical-align: top;
            display: inline-block;
            text-align: center;
        }
    	.caption {
            display: block;
        }
        .zoom {
          padding: 5px;
          transition: transform .2s;
          margin: 0 auto;
        }
        .zoom:hover {
          -ms-transform: scale(1.05); /* IE 9 */
          -webkit-transform: scale(1.05); /* Safari 3-8 */
          transform: scale(1.05); 
        }
         """)
    
    with doc:
        with div(cls="box",id="box"):
            with div(cls="imgBox"):
                for url in img_urls:
                    with a(href=url):
                        with figure(cls="item"):
                            with div(cls="zoom"):
                                img(src=url)
                                # replace the description here
                                figcaption("A very very very very very very long description",cls="caption")

    return doc

if __name__ == "__main__":
    img_urls = readURLs()
    html=generate_html(img_urls)
    Html_file= open("image_thumbnail.htm","w")
    Html_file.write(str(html))
    Html_file.close()
    
    images = loadImages(img_urls)
    thumbnail=generate_thumbnail(images)
    thumbnail.save("image_thumbnail.jpg")
    
    #thumbnail.show()
    webbrowser.open("image_thumbnail.htm")
    

    
    