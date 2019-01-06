import pymysql
print("pymysql 准备完成")
con = pymysql.connect(host='localhost', user='root', passwd='root', charset='utf8' )
cur = con.cursor()
print("获取光标")
cur.execute("use actire_db;")
print("数据库连接")
sql_insert = 'insert into admin_tbl (admin_id,admin_name,admin_password) values(11,11,md5(1));'
cur.execute(sql_insert)