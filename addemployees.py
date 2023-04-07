import mysql.connector


class emp:

    @staticmethod
    def getemp(self):

        emp = mysql.connector.connect(host="localhost", user="root", passwd="", database="employee")

        cur = emp.cursor()

        try:
            empid = raw_input("enter the employee id          :")
            empname = raw_input("enter the employee name      :")
            empdes = raw_input("enter the emplyee designation :")

            sql = "insert into addemp(empid,empname,empdes)values(%s,%s,%s)"
            val = [empid, empname, empdes]
            cur.execute(sql, val)
            print(cur.rowcount, "Record susccessfully added")
            emp.commit()

        except:
            print("synax error!!!")
