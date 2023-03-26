import pymysql as SQL
try:
    conn = SQL.connect(host="localhost",port=3306,user="root",passwd="your pass here",database="licdb")
    smt = conn.cursor()
    
    pn = input("Enter policy number(10 digits): ")
    cn = input("Enter Customer name : ")
    pt = input("Enter Plan term (in years): ")
    payt = input("Enter Payment type (m-> monthly,q-> quaterly,y-> yearly ): ")
    md = input("Enter maturity date (yyyy/mm/dd): ")
    sa = input("Enter Sum Assured : ")
    mn = input("Enter mobile no.(only 10 digits): ")
    an = input("Enter Agent name : ")
    np = input("Enter no. of policies : ")
    ida = input("Enter Agent ID : ")
    q = "insert into lict values({0},'{1}',{2},'{3}','{4}',{5},{6},'{7}',{8},{9})".format(pn,cn,pt,payt,md,sa,mn,an,np,ida)
    print(q)
    smt.execute(q)
    conn.commit()
    print("Data submitted Successfully")
    conn.close()
except Exception as e:
    print("Error",e)
