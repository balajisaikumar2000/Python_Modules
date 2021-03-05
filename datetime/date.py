import datetime

#d = datetime.date(2020,07,11)
d = datetime.date(2020,7,11)
tdy = datetime.date.today()

print(d)
print(tdy)
print(tdy.day)
print(tdy.year)
print(tdy.month)

print(tdy.weekday())          #for this type Monday is 0 and Sunday is 6
print(tdy.isoweekday())      #for this type Monday is 1 and Sunday is 7

#time delta is difference between time or date
tdelta = datetime.timedelta(days=7)

print(tdy + tdelta)       #seven days from now
print(tdy - tdelta)        #seven days back from now

bdy = datetime.date(2020,12,28)
till_bday = bdy - tdy
print(till_bday)                   #it gives the difference between our bdy and current day   ans)-72 days
print(till_bday.days)              #this will give the difference in just number            ans)-72
print(till_bday.total_seconds())   #this will give difference in seconds

#strftime: datetime to string
#strptime: string to datetime
dt = datetime.datetime.today()
print(dt)
#changing format
#you have to check documentation for such formats
print(dt.strftime("%B %d,%y"))     #strftime is used to change the format of time ,and date

dt_str =  "October 17,20"
dt = datetime.datetime.strptime(dt_str,"%B %d,%y")         #paramters are first one is the string which we want to change and it's format,if we give wrong format then error will raise
print(dt)