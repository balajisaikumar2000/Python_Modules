import sqlite3
from employee import Employee

conn = sqlite3.connect("employee.db")

c = conn.cursor()      #..............?

#c.execute("""CREATE TABLE employees(
#             first text,
#             last text,
#             pay integer
#             )""")

emp1 = Employee("john","Doe",80000)
emp2 = Employee("Jane","Doe",90000)
print(emp1.first)
print(emp1.last)
print(emp1.pay)
#c.execute("INSERT INTO employees VALUES('{}','{}',{})".format(emp1.first,emp1.last,emp1.pay))
c.execute("INSERT INTO employees VALUES(?,?,?)",(emp1.first,emp1.last,emp1.pay))
conn.commit()

c.execute("INSERT INTO employees VALUES(:first,:last,:pay)",{'first':emp2.first,'last':emp2.last,'pay':emp2.pay})
conn.commit()

#c.execute("INSERT INTO employees VALUES('balaji','sai kumar',50000)")
c.execute("SELECT * FROM employees WHERE last=?",("sai kumar",))
print(c.fetchone())

c.execute("SELECT * FROM employees WHERE last=:last",{"last":"Doe"})
print(c.fetchall())

conn.commit()

conn.close()