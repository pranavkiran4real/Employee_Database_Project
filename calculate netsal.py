import mysql.connector

emp = mysql.connector.connect(host="localhost", user="root", passwd="", database="employee")

cur = emp.cursor()

sql="select * from  salary"
cur.execute(sql)
res=cur.fetchall()

for x in res:
    dsp=x[0]
    print ("Day per Sal : ",x[0])


pd=float(input("Enter P Days : "))


ns=pd*dsp

print ("Net Salary : ",ns)

emp.close()


