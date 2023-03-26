import pymysql as SQL
try:
    conn = SQL.connect(host="localhost",port=3306,user="root",passwd="2022",database="licdb",cursorclass=SQL.cursors.DictCursor)
    smt = conn.cursor()
    pno = input("Enter policy no. : ")
    q = "Select * from lict where policyno={0}".format(pno)
    smt.execute(q)
    row = smt.fetchone()
    if(row):
        print(row['policyno'],row['customername'],row['Planterm'],row['Paymenttype'],row['Maturity'],row['Sumassured'],row['Mobileno'],row['Agentname'],row['noofpolicy'],row['Agentid'])
        ch = input("Are u sure u want to delete the record (y/n) ? : ")
        if(ch=="y" or ch=="Y"):
            smt.execute("Delete from lict where policyno = {0}".format(pno))
            conn.commit()
            print("Record deleted Successfully")
            conn.close()
        else:
            print("Record not found")
except Exception as e:
    print("Error",e)