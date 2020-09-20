# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:06:41 2020

@author: Malcom
"""

import webbrowser
from tkinter import *
from PIL import Image,ImageTk
import urllib.request
import math

class element:
    def __init__(self, image, url):
        self.image=image
        self.url=url

    def openURL(self):
        webbrowser.open(self.url,new=2)
    
def readURLs():
    URLs=[]
    file=open('urls.txt','r')
    lines=file.readlines()
    
    for line in lines:
        if line[-1]=='\n':
            URLs.append(line[:-1])
        else:
            URLs.append(line)
    
    return URLs

def downloadImg(folder, URLs):
    element_size=(128,128)
    elements=[]
    for url in URLs:
        imgName = url.split('/')[-1]
        path=folder+imgName
        urllib.request.urlretrieve(url,path)
        img = Image.open(path)
        img.thumbnail(element_size)
        imgTK = ImageTk.PhotoImage(img)
        elements.append(element(imgTK,url))
        
    return elements
        
def initializePanel(root,elements):
    element_size=(128,128)
    container_size=(150,150)
    columns=(math.ceil(math.sqrt(len(elements))))
    
    panelWidth = container_size[0] * columns
    panelHeight = container_size[1] * int(math.ceil(len(elements) / columns))
    
    root.geometry(str(panelWidth)+'x'+str(panelHeight))
    
    row=0
    col=0
    
    for element in elements:
        locationX = container_size[0] * col + int((container_size[0] - element_size[0])/2)
        locationY = container_size[1] * row
        
        btn=Button(root, image=element.image, command=element.openURL)
        btn.place(x=locationX, y=locationY, in_=root)
        
        col += 1
        
        if col == columns:
            row += 1
            col = 0
            
            

if __name__ == "__main__":
    root=Tk()
    
    folder='download/'
    URLs=readURLs()
    elements=downloadImg(folder,URLs)
    initializePanel(root,elements)
    
    root.mainloop()
    
    