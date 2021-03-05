#we use Dunder methods whenever we face a object in print statement ,what exactly they do is they alter the code and will result in what we expect
#and below methods can available in documnetation
class Employee:
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    def __add__(self,other):                                                      #print(emp_1 + emp_2)
        return self.pay + other.pay                                             #emp_1 is self.pay and other pay is emp_2,

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Balaji","Sai Kumar",50000)
emp_2 = Employee("Test","User",60000)

print(emp_1)
#first when we print this we will get object
#when we mention repr,str ,dunders in class we will get what is return in the dunder menthods
#if both dunders(repr,str) return there respective last dunder in class will be return
print(repr(emp_1))                  #we can get respective dunder return by mentioning like this
print(str(emp_1))

print(emp_1.__repr__())              #this  same as above
print(emp_1.__str__())

#see example below dunder methods for understanding of this

print(emp_1 + emp_2)                #we will get error if we won't mention add dunder in our  class

print(len(emp_1))                    #we will get error if we won't mention len dunder in our  class

"""    Dunder add   """
#say for example:
print(1 +2)
#what happens when print out the above statement is:--
print(int.__add__(1,2))

#like wise strings have thier own Dunder method:
print("a" + "b")
#what happens when print out the above statement is:--
print(str.__add__("a","b"))                                 #Dunder add

""" Dunder len"""
print(len("test"))

#is similar to:
print("test".__len__())
print(str.__len__("test"))