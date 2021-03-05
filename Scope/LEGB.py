""" scope always goes through LEGB -----local,enclosing,global,built-in"""

import builtins

#print(dir(builtins))

x = "global x"

def test():
    x = "local x"
    print(x)

test()
print(x)

print("------------------------------------------------------------------------------------------------")
x = "global x"


def test1():
    global x
    x = "local x"
    print(x)

test1()
print(x)
print("------------------------------------------------------------------------------------------------")

#enclosing: means inclusing other function inside other function
def outer():
    x = "outer x"

    def inner():
        x ="inner x"
        print(x)
    inner()
    print(x)
outer()

print("------------------------------------------------------------------------------------------------")

def outer():
    x = "outer x"

    def inner():
        nonlocal x          #here nonlocal changes the local variable i.e "x"
        x ="inner x"
        print(x)
    inner()
    print(x)
outer()