import pymysql
import logs
con = pymysql.connect(host='localhost', user='root', passwd='root', database='actire_db', charset='utf8')
cursor = con.cursor()
sql_updata = "UPDATE type_tbl SET admin_name='admin',admin_login_name='user123' WHERE admin_id= 25 ;"
cursor.execute(sql_updata)
logs.logs_on("执行更新操作，SQL")
logs.logs_on(sql_updata)
con.commit()
cursor.close()
con.close()
