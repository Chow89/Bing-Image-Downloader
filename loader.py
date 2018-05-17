#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import time
import json
import os
import inspect
import requests

ts = str(round(time.time() * 1000))
url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=" + ts

# get json with image url from url
res = requests.get(url).content
j = json.loads(res)

# create url for 1920x1080
imageurl = ("http://www.bing.com" + j.get('images')[0]['url'])

# create filename for local files
imageurlsplitted = imageurl.split("/")
imageurlsplitted.reverse()
filename = datetime.datetime.now().strftime('%Y-%m-%d') + " - " + imageurlsplitted[0].split("_")[0]
extension = imageurlsplitted[0].split(".")[1]

# get and save images
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
if not os.path.isdir(path + "/images/1920x1080"):
    os.makedirs(path + "/images/1920x1080")
if not os.path.isfile(path + "/images/1920x1080/" + filename + "." + extension):
    imagebig = requests.get(imageurl).content
    open(path + "/images/1920x1080/" + filename + "." + extension, "wb").write(imagebig)
