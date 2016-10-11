#!/usr/bin/env python
#coding=utf8

import httplib

httpClient = None

import hashlib
def md5(str):
    import hashlib
    m = hashlib.md5()   
    m.update(str)
    return m.hexdigest()

try:
    httpClient = httplib.HTTPConnection('https://10.101.13.169', 80, timeout=10)
    fileId="fV-2mDeIT6y8GcwwaciACwAAAAUAAQED"
    fileName="test.pptx"

    fileName=fileName.encode('utf8') 
    fileId=fileId.encode('utf8') 
    appKey="1435129452994"
    appName="wirelessprojection"
    ftime="1435128182247"

    token=md5(appName+appKey+fileId+ftime)
    param = "ftime=1435128182247&source="+ fileId+ "&appName=wirelessprojection&" + "fileName="+fileName+"&"+"token="+token 
    print "param: \n"+param
    httpClient.request('GET', '/getPreviewUrl' + "?" + param)
    #httpClient.set_debuglevel(1)

    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()


