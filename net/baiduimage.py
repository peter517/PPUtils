#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import urllib
import json
from urllib import quote
import socket
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 设置超时
socket.setdefaulttimeout(10)

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
    if os.path.exists(wordDirPath + "/" + str(counter) + ".jpeg"):
        counter = index
    check = '<html><body><h1>403 Forbidden</h1>'
    print "name " + word + " imagePath " + imagePath

    for info in json['imgs']:
        urllib.urlretrieve(info['objURL'], './' + word + '/' + str(counter) + '.jpeg')
        # 判断防爬虫 <html><body><h1>403 Forbidden</h1>
        fp = open("./" + word.replace("?","") + "/" + str(counter) + ".jpeg")
        if not cmp(fp.readline(), '<html><body><h1>403 Forbidden</h1>\n'):
            os.remove("./" + word + "/" + str(counter) + ".jpeg")
            counter -= 1
        fp.close()
        counter += 1

        print "+1，已经保存" + str(counter - 1)
        if counter > max_number:
            return
    return counter

# 获取后缀名
def getFix(name):
    return name[name.find('.'):]

# 获取前缀
def getPrefix(name):
    return name[:name.find('.')]

# print getFix('123.txt')
# getImagesURL(390,'美女')
file_object1 = open("../test/diff_not_include.txt", 'r')

try:
    srcList = file_object1.readlines()
finally:
    file_object1.close()

for src in srcList:
    print "getImagesURL " + src
    try:
        getImagesURL(10, src)
    except Exception as e :
        print e

