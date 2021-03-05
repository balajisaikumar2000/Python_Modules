#unpacing values
#unpacking:
a,b = (1,2)

print(a)
print(b)

"""       #this will raise an error
a,b,c =  (1,2,3,4,5)
print(a)
print(b)
print(c)    """
#--------------------
a,b,*c =  (1,2,3,4,5)    #this works fine
print(a)
print(b)
print(c)

#---------------------
a,b,*_ =  (1,2,3,4,5)    #this works fine
print(a)
print(b)
#--------------
a,b,*c,d =  (1,2,3,4,5,6)
print(a)
print(b)
print(c)
print(d)
#-------------------------------
a,b,*_,d =  (1,2,3,4,5,6,7)
print(a)
print(b)
print(d)


