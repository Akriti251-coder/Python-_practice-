#def is used for defining the function
"""def abcd():
    print("FF")
abcd()"""

#This is a python program to add two numbers
"""def addnum(a,b):
    print("Sum is ",a+b)
addnum(10,20)
addnum(30.9,40.8)"""

#return is used to send a result back from a function
"""def sum(a,b):
    c = a+b
    return c

x=sum(1,2)
print("Sum of two variables is:",x)"""

"""def m1():
    print("This function is returning nothing")
m1()
x=m1()
print(x)"""

"""def m1(a,b):
    c = a + b
    d = a - b
    return c,d
x,y = m1(10,5)
print("sum of a and b:",x)
print("subtraction of a and b:",y) """

"""def m1():
    print("first function information")
def m2():
    print("second function information")
    m1()
m2()"""

"""def add():
    print("We assigned function to variable")
sum = add
sum()"""

#to bring a function into another 
"""def display(x):
    print("This is display function")
def message():
    print("This is a message function")
display(message)"""

"""def message(text):
    print(text)
def printmessage(x):
    x("Hello World")
printmessage(message)"""