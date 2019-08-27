import pymysql.cursors
import sys
print("pymysql 准备完成")
con = pymysql.connect(host='localhost', user='root', passwd='root', charset='utf8')
cursor = con.cursor()
print("获取光标")
cursor.execute("use actire_db;")
print("数据库连接")
sql_insert = 'insert into admin_tbl (admin_name,admin_password) values(11,md5(1));'
cursor.execute(sql_insert)
print("sql语句执行完成")
