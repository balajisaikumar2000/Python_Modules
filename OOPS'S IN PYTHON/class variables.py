class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)          #or we can use Employee.raise_amount

print(Employee.num_of_emps)                            #we will get 0 because we didn't initated yet
emp_1 = Employee("Balaji","Sai Kumar",50000)
emp_2 = Employee("Test","User",60000)

print(Employee.num_of_emps)                         #we will get 2 cause ,we initated two employess

print(emp_1.pay)
print(emp_1.apply_raise())    #it doesn't print anything because it just assign value to the pay
print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)         #in emp_1 we don't have any raise amount variable ,it accessing from class,beacuse we have like this in our code emp_1 = Employee
print(Employee.__dict__)          #here class have raise_amount variable ,which is class varible

#if we change the varible in class
Employee.raise_amount = 2.0
print(Employee.raise_amount)
print(emp_1.raise_amount)         #instances also changes because they are accessing the variables from class
print(emp_2.raise_amount)

emp_1.raise_amount = 3.0
print(Employee.raise_amount)
print(emp_1.raise_amount)          #only emp_1 changed ,beacuse
print(emp_2.raise_amount)          # we didn't changed them in class variabls
print(emp_1.__dict__)              #we will get raise amount in emp_1 because we asssigned externally

emp_1.apply_raise()
print(emp_1.pay)         #52000 * 3 = 15600





