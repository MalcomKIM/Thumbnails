# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:39:41 2020

@author: Malcom
"""

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


def generate_html(video_urls):
    doc = dominate.document(title='Video Thumbnails')
    
    with doc.head:
        style("""
        *{
            margin: 0;
            padding: 5;
        }
        .box{
            display: flex;
            flex-wrap: wrap;
        }
        .box:after{
            content: '';
            flex-grow: 99999;
    	}
    	.videoBox{
                flex-grow: 1;
                margin: 5px;
    	}
        iframe {
            width: 420px;
            height: 315px;
            float: left;
            margin: 5px 10px;
        }

         """)
    
    with doc:
        with div(cls="box",id="box"):
            with div(cls="videoBox"):
                for url in video_urls:
                    iframe(allowfullscreen="allowfullscreen", src=url)
    return doc
    

if __name__ == "__main__":
    
    video_urls = readURLs()
    
    html=generate_html(video_urls)
    Html_file= open("video_thumbnail.html","w")
    Html_file.write(str(html))
    Html_file.close()
    
    webbrowser.open("video_thumbnail.html")
    
