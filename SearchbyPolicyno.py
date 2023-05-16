import pymysql as SQL
try:
    conn = SQL.connect(host="localhost",port=3306,user="root",passwd="your pass here",database="licdb",cursorclass=SQL.cursors.DictCursor)
    smt = conn.cursor()
    pno = input("Enter policy no. : ")
    q = "Select * from lict where policyno={0}".format(pno)
    smt.execute(q)
    row = smt.fetchone()
    if(row):
        print("Policy no.",row['policyno'])
        print("1] Customer name : ",row['customername'])
        print("2] Plan term : ",row['Planterm'])
        print("3] Payment type : ",row['Paymenttype'])
        print("4] Maturity : ",row['Maturity'])
        print("5] Sumassured : ",row['Sumassured'])
        print("6] Mobile number : ",row['Mobileno'])
        print("7] Agent name : ",row['Agentname'])
        print("8] No. of policies : ",row['noofpolicy'])
        print("9] Agent ID : ",row['Agentid'])
    else:
        print("Record not found")
    conn.close()
except Exception as e:
    print("Error",e)
