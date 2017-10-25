import httplib
import json

httpClient = None

try:
    httpClient = httplib.HTTPConnection('ups.youku.com', 80, timeout=10)
    # httpClient.set_debuglevel(1)
    httpClient.request('GET', '/ups/wget.json?vid=XMjcxMzkwMjU3Mg==&who=gjwxb')

    response = httpClient.getresponse()
    # print response.status
    # print response.reason
    resultStr = response.read()
    # print resultStr
    resultJson = json.loads(resultStr)
    streamLen = len(resultJson['data']['stream'])

    segsList = resultJson['data']['stream'][streamLen - 1]['segs']
    # print(segsList)

    cdnList = []
    for i in range(0, len(segsList)):
        #print(segsList[i])
        cdnList.append(segsList[i]['cdn_url'])

    print " ".join(cdnList)
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()

