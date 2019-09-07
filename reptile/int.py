import urllib.request as urllib2
req = urllib2.Request("http://www.baidu.com")
res = urllib2.urlopen(req)
html =  res.read()
print(html)