import pymysql
print("pymysql 准备完成")

con = pymysql.connect(host='localhost', user='root', passwd='root', charset='utf8')
cur = con.cursor()
cur.execute("use actire_tbl;")
sql_insert = 'insert into admin_tbl (admin_id,admin_name,admin_password) values(11,11,md5(1));'
