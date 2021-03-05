class Person():
    pass

person1 = Person()

"""
person1.first = "Balaji"
person1.last ="Sai Kumar"

print(person1.first)      """

setattr(person1,"first","Balaji")          #object name,atrribute name,value

print(person1.first)
print(getattr(person1,"first"))     #THIS WORKS SAME         ,#object name,atrribute name

#seconds example:
person = Person()

person_info  ={"first":"Balaji","last":"sai kumar"}

for key,value in person_info.items():
    setattr(person,key,value)
print(person.first)
print(person.last)

for key in person_info.keys():
    print(getattr(person,key))