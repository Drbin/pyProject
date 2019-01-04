import pymysql
print("pymysql 准备完成")

con = pymysql.connect(host='localhost', user='root', passwd='root', charset='utf8')
cur = con.cursor()
cur.execute("use admin_tbl;")
