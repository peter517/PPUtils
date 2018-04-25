#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import os
import socket
import urllib
from urllib import quote
import shutil


file_object = open("imgae_download_file.txt", 'r')

try:
    src = file_object.readlines()
    dir_name = "./image_download"
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.mkdir(dir_name)

    for item in src:
        imagePath = item.split("\t")[1]
        filePath = dir_name + "/" + item.split("\t")[0] + ".jpeg"
        print "imagePath " + imagePath + " filePath " + filePath
        urllib.urlretrieve(imagePath, filePath)

finally:
    file_object.close()


