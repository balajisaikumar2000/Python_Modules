"""
when we did this ,it works fine but we have to print like this print(emp_1.email())
but we want email as variable(variable is called "property" in javascript
    def email(self):
        return '{} {}@email.com'.format(self.first,self.last)            """

class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last
#we can solve above problem by addingn @property to above the def
    @property
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):                                              #we can change the fullname to a attribute by adding @property,so we do not have to  metionn like this--print(emp_1.fullname()),,,,,,we have to mention like this print(emp_1.fullname)
        return "{} {}".format(self.first,self.last)

    @fullname.setter                                           #if we want to alter the function,we have to setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter                           #if we want to delete property we have to follow like this
    def fullname(self):
        print("Deleted....!")
        self.first = None
        self.last = None

emp_1 = Employee("Balaji","Sai Kumar")

emp_1.first  = "Shyam"

emp_1.fullname = "swathi munagpati"        #we will get error when we do this(AttributeError: can't set attribute) to solve this we have to set @fullname.setter

print(emp_1.first)
print(emp_1.email)                      #here on output first property changed ,but email didn't changed ,so we will make some minor changes in the code
print(emp_1.fullname)

del emp_1.fullname                 #here fullname will only deleted because we set the deleter to only fullname


