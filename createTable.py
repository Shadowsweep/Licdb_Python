import pymysql as SQL
try:
    conn = SQL.connect(host="localhost",port=3306,user="root",passwd="Your password here",database="licdb")
    smt = conn.cursor()
    q="Create Table lict(policyno int primary key,customername varchar(50),Planterm decimal(10),Paymenttype varchar(50),Maturity date,Sumassured decimal(10),Mobileno decimal(10),Agentname varchar(50),noofpolicy decimal(10),Agentid decimal(10))"
    smt.execute(q)
    conn.commit()
    print("Table created Successfully")
    conn.close()
except Exception as e:
    print("Error",e)