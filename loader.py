#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
import os
import inspect

import urllib3


ts = str(round(time.time() * 1000))
url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=" + ts
http = urllib3.PoolManager()

# get json with image url from url
res = http.request('GET', url).data.decode("utf-8")
j = json.loads(res)

# create url for 1920x1080 and 1366x768 image
imageurlbig = ("http://www.bing.com" + j['images'][0]['url'])
imageurlsmall = imageurlbig.replace("1920x1080", "1366x768")

# create filename for local files
imageurlsplitted = imageurlbig.split("/")
imageurlsplitted.reverse()
filename = imageurlsplitted[0].split("_")[0]
extension = imageurlsplitted[0].split(".")[1]

# get and save images
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
if not os.path.isdir(path + "/images/1920x1080"):
    os.makedirs(path + "/images/1920x1080")
if not os.path.isdir(path + "/images/1366x768"):
    os.makedirs(path + "/images/1366x768")
if not os.path.isfile(path + "/images/1920x1080/" + filename + "." + extension):
    imagebig = http.request('GET', imageurlbig)
    open(path + "/images/1920x1080/" + filename + "." + extension, 'wb').write(imagebig.data)
if not os.path.isfile(path + "/images/1366x768/" + filename + "." + extension):
    imagesmall = http.request('GET', imageurlsmall)
    open(path + "/images/1366x768/" + filename + "." + extension, 'wb').write(imagesmall.data)
