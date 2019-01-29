import pymysql
import logs
con = pymysql.connect(host='localhost', user='root', passwd='root', database='actire_db', charset='utf8')
cursor = con.cursor()
sql_read = "SELECT * FROM admin_tbl"


