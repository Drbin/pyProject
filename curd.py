import pymysql.cursors
import sys
print("pymysql 准备完成")
con = pymysql.connect(host='localhost', user='root', passwd='root', database='actire_db', charset='utf8')
cursor = con.cursor()
sql_insert = "insert into admin_tbl(admin_name,admin_login_name,admin_password,admin_create) values (11,1,md5(1),NOW())"
cursor.execute(sql_insert)
print(cursor.execute(sql_insert))

cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
cursor.close()
con.close()

