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



# 设置超时
socket.setdefaulttimeout(20)

# 获取图片url内容等
def getImagesURL(max_number, word='美女'):
    search = quote(word)
    pn = 0
    while pn <= max_number:
        url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' + search + '&cg=girl&pn=' + str(
                pn) + '&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
        page = urllib.urlopen(url)
        data = page.read()
        data = json.loads(data)
        saveImage(data, word, max_number)
        pn += 60

# 保存图片
def saveImage(json, word, max_number):
    counter = 1
    wordDirPath = "./" + word.strip('\n')
    if not os.path.exists(wordDirPath):
        os.mkdir(wordDirPath)
    # 判断名字是否重复
    index = len(os.listdir(wordDirPath))
    imagePath = wordDirPath + "/" + str(counter) + ".jpeg";

    if os.path.exists(imagePath):
        counter = index

    for info in json['imgs']:
        imagePath = wordDirPath + "/" + str(counter) + ".jpeg";
        urllib.urlretrieve(info['objURL'], imagePath)
        # 判断防爬虫 <html><body><h1>403 Forbidden</h1>
        fp = open(wordDirPath + "/" + str(counter) + ".jpeg")
        if not cmp(fp.readline(), '<html><body><h1>403 Forbidden</h1>\n'):
            os.remove(imagePath)
            counter -= 1
        fp.close()
        counter += 1
        print "+1 save image total " + str(counter - 1)
        if counter > max_number:
            return

    return counter


# Main
try:
    words_file = open("../test/diff_not_include.txt", 'r')
    word_lines = words_file.readlines()
    for word in word_lines:
        print "getImagesURL word " + word
        try:
            getImagesURL(20, word)
        except Exception as e:
            print e
finally:
    words_file.close()

