import itertools

counter = itertools.count(start=5,step=-2.5)     #initially starts from 0,we can set step to +ve also

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


data = [100,200,300,400]
daily_data = list(zip(itertools.count(),data))   #itertools.count() is useful for mentioning the index it just like enumerate function
#zip is an object so we have to convert them into list
print(daily_data)

data = [100,200,300,400]
daily_data = list(zip(range(10),data))    #if data doesn't insufficient it doesn't print it out
print(daily_data)

#itertools.zip_longest() :
data = [100,200,300,400]
daily_data = list(itertools.zip_longest(range(10),data))        #it prints None if data exceeds
print(daily_data)

#itertools.cycle():
counter = itertools.cycle([1,2,3])   #counter = itertools.cycle(["ON",OFF"])
print(next(counter))
print(next(counter))                        #it revolve around the list only
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#itertools.repeat()
counter = itertools.repeat(2)              #  will repeat mentioned number only
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

"""        #we will get stopiteration
counter = itertools.repeat(2,times=3)         #we can mention how many times we want
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))     """

#map:
#squares is a object either list or tuple etc..,
squares = map(pow,range(10),itertools.repeat(2))    #pow is a built in function,#first paramter is  function,second one is theinput values,third is another paramter for pow() function which says to whicbh we wan the power
print(list(squares))

#itertools.starmap():
squares = itertools.starmap(pow,[(0,2),(1,2),(2,3)])     #list of tuples,we can also give lists as input
print(list(squares))








