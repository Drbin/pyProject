from urllib import request
import logs
def d(url):
    print("地址： %s" % url)
    resp = request.urlopen(url)
    data = resp.read()
    f = open("file.html","wb")
    f.write(data)
    f.close()
    logs.file_on("在 %s 获取了数据 并插入 file.html中" % url)
    print("%d b 数据来源于 %s" %(len(data),url))
    return 0
d(url='https://www.baidu.com')



