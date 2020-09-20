# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:39:41 2020

@author: Malcom
"""

from pytube import YouTube
import webbrowser
import dominate
from dominate.tags import *


def readURLs():
    video_urls = []
    file = open('urls.txt', 'r')
    lines = file.readlines()

    for line in lines:
        if line[-1] == '\n':
            video_urls.append(line[:-1])
        else:
            video_urls.append(line)

    return video_urls


def get_thumbnails(URLs):
    matches = []
    for url in URLs:
        try:
            yt = YouTube(url)
            tnURL = yt.thumbnail_url
            matches.append([tnURL,url])
        except:
            continue

    return matches

def generate_html(matches):
    doc = dominate.document(title='Video Thumbnails')

    with doc.head:
        style("""\
        * {
          box-sizing: border-box;
        }

        .column {
          float: left;
          width: 33.33%;
          padding: 5px;
        }

        /* Clearfix (clear floats) */
        .row::after {
          content: "";
          clear: both;
          display: table;
        }
         """)
        
    with doc:
        with div(Class='row'):
            for match in matches:
                with div(Class='column'):
                    with a(href=match[1]):
                        img(border="0",src=match[0],style="width:100%")
    
    return doc
    

if __name__ == "__main__":
    
    video_urls = readURLs()
    matches = get_thumbnails(video_urls)
    
    html=generate_html(matches)
    Html_file= open("video_thumbnail.htm","w")
    Html_file.write(str(html))
    Html_file.close()
    
    webbrowser.open("video_thumbnail.htm")
    
