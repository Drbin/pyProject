from urllib import request
from logs import file_on
def d(url):
    print("地址： %s" % url)
    resp = request.urlopen(url)
    data = resp.read()
    f = open("file.html","wb")
    f.write(data)
    f.close()
    file_on("在 %s 获取了数据 并插入 file.html中 \n" % url)

    return 0
d(url='https://www.baidu.com')



