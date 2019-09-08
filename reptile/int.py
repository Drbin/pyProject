import urllib.request as urllib2
headers = {"User-Agent":""}#user Agent 是反爬虫第一步

req = urllib2.Request("https://www.baidu.com/s?wd=urllib2&rsv_spt=1&rsv_iqid=0xaf7c35520012da13&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_dl=tb&rsv_enter=0&rsv_n=2&rsv_sug3=1&rsv_sug1=1&rsv_sug7=100&prefixsug=urllib2&rsp=1&inputT=1897&rsv_sug4=1897&rsv_sug=1",headers = headers)
res = urllib2.urlopen(req)
html =  res.read()
wd = {"wd" : "测试数据"}
print(urllib2.pars_list(wd))# python2 urlencode
code = res.getcode()
print(code)
#http 响应码
print(res.geturl())# 返回实际数据的地址
print(res.info())
print(html)