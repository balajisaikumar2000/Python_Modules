#regular methods deals with instances
#class methods deals with classes
#static methods deals with other than class,and regular ,they can easily identitable

class Employee:
    num_of_emps = 0                 #these are class variables
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split("-")
        return  cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True

emp_1 = Employee("Balaji","Sai Kumar",50000)
emp_2 = Employee("Test","User",60000)

#Employee.set_raise_amt(1.05)
emp_1.set_raise_amt(2.0)             #it works because call to the set_raise_amt will change class's raise_amt variable,because it has relationship with class like this:- emp_1 = Employeee(x,y,z)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

#first,last,pay  = emp_str_1.split("-")

#for clear code we don't have split every string that we want to pass into the class,so we simply pass them into class  methods
new_emp_1 = Employee.from_string(emp_str_2)      #what will be returned here internally is cls(first,last,pay)----Employee(first,last,pay)

print(new_emp_1.email)
print(new_emp_1.first)

import datetime

my_date = datetime.date(2016,7,11)

#they work with both class and instance because they are independent on both them but it need atleast one of them to access
print(Employee.is_workday(my_date))
print(emp_1.is_workday(my_date))

