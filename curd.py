import pymysql.cursors
import sys
print("pymysql 准备完成")
con = pymysql.connect(host='localhost', user='root', passwd='root', charset='utf8')
cursor = con.cursor()
print(cursor)
print("获取光标")
cursor.execute("use actire_db;")
print("数据库连接")
sql_insert = "insert into admin_tbl(admin_name,admin_login_name,admin_password,admin_create) values (11,1,md5(1),NOW())"
cursor.execute(sql_insert)
print("sql语句执行完成")
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

