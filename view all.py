import mysql.connector
emp=mysql.connector.connect(host="localhost",user="root",passwd="",database="employee")

cur=emp.cursor()
try:
    view="select * from addemp"
    cur.execute(view)
    result=cur.fetchall()
    print("empid\t\tempname\t\tempdes\t\tdayspres\t\tnetsal")
    for x in result:
        print("%s\t%s\t%s\t%s\t%.s"%(x[0],x[1],x[2],x[3],x[4]))
except:
    print("viewing error")
