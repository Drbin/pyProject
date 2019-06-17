from urllib import request

def d(url):
    print("地址： %s" % url)
    resp = request.urlopen(url)
    data = resp.read()
    f = open("jd.html","wb")
    f.write(data)
    f.close()
    print("%d b 数据来源于 %s" %(len(data),url))
d(url='https://www.baidu.com')

 