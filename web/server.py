import cgi, cgitb

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()
#BASE_DIR =  os.path.dirname(os.path.abspath(__file__))
site_url  = form.getvalue('url')
print(site_url)

def admin():

    with open('index.html','r') as fd:
        data = fd.read()
    return data
admin()
