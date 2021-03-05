
#this is a bad practise
"""
names = ["balaji","shyam","durga","bhavani"]

index  =0
for name in names:
    print(index,name)
    index += 1         """


names = ["balaji","shyam","durga","bhavani"]

"""
for index,name in enumerate(names):
    print(index,name)           """

for index,name in enumerate(names,start=1):
    print(index,name)