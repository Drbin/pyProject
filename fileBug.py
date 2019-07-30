from urllib import request
from logs import file_on
def download_file(txt,url):
    print("地址： %s" % url)
    resp = request.urlopen(url)
    data = resp.read()
    f = open(txt ,"wb")
    f.write(data)
    f.close()
    file_on("在 %s 获取了数据 并插入 file.html中 \n" % url)
    return 0

