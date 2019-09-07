import urllib.request as urllib2
headers = {"User-Agent":""}#user Agent 是反爬虫第一步

req = urllib2.Request("http://www.baidu.com",headers = headers)
res = urllib2.urlopen(req)
html =  res.read()
code = res.getcode()
print(code)
#http 响应码

print(html)