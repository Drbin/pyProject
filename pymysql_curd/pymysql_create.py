import pymysql.cursors
import sys
import logs
con = pymysql.connect(host='localhost', user='root', passwd='root', database='actire_db', charset='utf8')
cursor = con.cursor()
sql_insert = "insert into admin_tbl(admin_name,admin_login_name,admin_password,admin_create) values (11,1,md5(1),NOW())"
logs.logs_on("执行了插入，SQL语句："+sql_insert)
logs.logs_on
cursor.execute(sql_insert)
con.commit()
cursor.close()
con.close()
