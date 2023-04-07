import mysql.connector

emp=mysql.connector.connect(host="localhost",user="root",passwd="",database="employee")

cur=emp.cursor()

try:
    salperday=raw_input("enter the salary per day      :")
    sql="insert into salary values(%s)"
    val=[salperday]
    cur.execute(sql,val)
    print(cur.rowcount,"Record susccessfully added")
    emp.commit()

except:
    print("syntax error!!!")

