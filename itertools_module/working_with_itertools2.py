import itertools
import operator

letters = ["a","b","c","d"]
numbers = [0,1,2,3]
names = ["Balaji","sai kumar"]

result = itertools.combinations(letters,2)   #order doesn't matter means:-the tuple with same values but different order won't considerable
#since result is a object ,we have to loop over it,the SECOND parameter is saying we want list/tupel containing two values
for item in result:
    print(item)
print("------------------------------------------------------------------------------------------------------")

letters = ["a","b","c","d"]
numbers = [0,1,2,3]
names = ["Balaji","sai kumar"]

result = itertools.permutations(letters,2)   #ordermatter means:-the tuple with same values but different order will  considerable

for item in result:
    print(item)

print("------------------------------------------------------------------------------------------------------")
result = itertools.product(numbers,repeat=2)      #permutations and combinations doesn't include themselves means like-(0,0) for this we can use product()

for item in result:
    print(item)
print("------------------------------------------------------------------------------------------------------")
#this works same as product but we are doing with combinations_with_replacement
#or:
result = itertools.combinations_with_replacement(numbers,4)

for item in result:
    print(item)

print("------------------------------------------------------------------------------------------------------")

#itertools.chain()
combined = itertools.chain(letters,numbers,names)  #this all lists mentioned in chain():-letters,numbers,names will be present in combined variable and we can retrieve informationof all mentioned lists once at all ,and it(combined)doesn't store it permanently
                                                     #that's why where it is useful ,not by  just doing combined = letter+numbers+names ,because this method stores it permanently
for item in combined:
    print(item)

print("------------------------------------------------------------------------------------------------------")
#islice:
result = itertools.islice(range(10),1,5,2)  #by default when mention only one number here it is 5 ,it says that we want upto "5",when we mentin before 5 it is starting point,at last parameter is "step"
for item in result:
    print(item)


with open("demo.log","r") as f:
    header = itertools.islice(f,3)

    for line in header:
        print(line,end="")
#------------------------------------------------------------------
#itertools.compress():
#it just works like filter
selectors = [True,True,False,True]
#first parameter will be printed and second one is for comparison
result  = itertools.compress(letters,selectors)    #it takes two lists/tuples and compares and results when "True"

for item in result:
    print(item)

#filter:
def lt_2(n):
    if n <2:
        return  True
    else: False
result =  filter(lt_2,numbers)
for item in result:
    print(item)

print("------------------------------------------------------------------------------------------------------")

#filterfalse:                             #results  false statements
result =  itertools.filterfalse(lt_2,numbers)
for item in result:
    print(item)

print("------------------------------------------------------------------------------------------------------")

numbers = [0,1,2,3,2,1,0]
result = itertools.dropwhile(lt_2,numbers)      #when they(dropwhile()) gets false it will result false ones's
for item in result:
    print(item)

print("------------------------------------------------------------------------------------------------------")

result = itertools.takewhile(lt_2,numbers)       #it is same as dropwhile() except this takes true one's
for item in result:
    print(item)

print("------------------------------------------------------------------------------------------------------")
#add:
result = itertools.accumulate(numbers)            #will adds along the list ,and returns the result there itself,for clarification run the code,defaultly it will add ,there is no other arthimetic operators like mul,sub.div
for item in result:
    print(item)
#for multiplication:
numbers = [1,2,3,2,1,0]
result = itertools.accumulate(numbers,operator.mul)          #if we want extra arthimetic operators we have to import operrator module
for item in result:
    print(item)



