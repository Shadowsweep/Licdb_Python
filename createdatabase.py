import pymysql as SQL
try:
    conn = SQL.connect(host="localhost",port=3306,user="root",passwd="2022")
    smt = conn.cursor()
    q="create database licdb"
    smt.execute(q)
    conn.commit()
    print("Database created Successfully")
    conn.close()
except Exception as e:
    print("Error",e)