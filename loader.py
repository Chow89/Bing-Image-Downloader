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
res = http.request('GET', url).data.decode("utf-8")
j = json.loads(res)
imageurl = ("http://www.bing.com" + j['images'][0]['url'])
imageurlsplitted = imageurl.split("/")
imageurlsplitted.reverse()
filename = imageurlsplitted[0]
image = http.request('GET', imageurl)
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
if not os.path.isdir(path + "/images"):
    os.makedirs(path + "/images")
if not os.path.isfile(path + "/images/" + filename):
    open(path + "/images/" + filename, 'wb').write(image.data)
