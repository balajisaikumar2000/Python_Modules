first_name = "balaji"
last_name = "sai kumar"

sentence = "My name is {} {}".format(first_name,last_name)
sentence2 = "My name is {1} {0}".format(first_name,last_name)
print(sentence)
print(sentence2)

#second method:
sentence = f"My name is {first_name} {last_name}"       #we are telling that it is a f-string,in place holders variables should be mentioned
print(sentence)
#-------------------
sent = f"My name is {first_name.upper()} {last_name.lower()}"
print(sent)

#Working with dictionaries:
person = {"name":"balaji","age":20}
#with format method:
sentence_dict = "My name is {} and I am {} years old".format(person["name"],person["age"])
print(sentence_dict)

#with f-string:
sentence_f = f'My name is {person["name"]} and I am {person["age"]} years old'
print(sentence_f)

#calculation:
#whenever we want to do some calculations we have to mention them in placeholders
calculation = f'4times 11 is equal to { 4 * 11}'
print(calculation)

#looping:
for n in range(1,11):
    sentence = f'The value is {n}'
    print(sentence)

#adding some formatting:
for n in range(1,11):
    sentence = f'The value is {n:02}'   #what we have done is we are mentioning colon in place holders i.e we are formatting them(the thing in place holders)i.e we are converting the parameter before the colon into format which is after the colon
    #here the we are converting the numbers into two digits i.e 01,02,03 like that
    print(sentence)

#pi:
pi = 3.14159265

sentence = f'Pi is equal to {pi:.4f}'  #we are converting it to 4 digit float value and it is rounding it off itself
print(sentence)

from  datetime import datetime

birthday = datetime(1990,1,1)        #default format is year-month-date

sentence = f'Jenn has a birthday on {birthday}'
sentence_for = f'Jenn has a birthday on {birthday:%B %d,%Y}'    #we are  converting it to day-date-year  format
print(sentence)
print(sentence_for)
