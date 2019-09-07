import urllib.request as urllib2
headers = {"User-Agent":""}
req = urllib2.Request("http://www.baidu.com",headers = headers)
res = urllib2.urlopen(req)
html =  res.read()
print(html)