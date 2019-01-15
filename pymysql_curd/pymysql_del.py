import pymysql
import logs
con = pymysql.connect(host='localhost', user='root', passwd='root', database='actire_db', charset='utf8')
cur = con.cursor()
sql_del = "DELETE FROM admin_tbl WHERE admin_id = '22'"
logs.logs_on("执行了删除操作，SQL语句为:")
logs.logs_on(sql_del)
cur.execute(sql_del)
con.commit()
cur.close()
con.close()
