#function can be assigned to a variable
"""def add(x,y):
    return x+y
sum=add
print(sum(10,20))"""

#function can be passed as an argument to another function
"""def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def process(func,x,y):
    return func(x,y)
print(process(add,10,20))
print(process(sub,10,20))"""

# function can be defined inside another function
"""def outer():
    print("Outer Function")
    def inner():
        print("Inner Function")
    inner()
outer()"""

#function can return another function
"""def outer():
    print("Outer Function")
    def inner():
        print("Inner Function")
    return inner
func=outer()
func()"""

"""def createfunctions():
    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
    return add,sub
add_function,sub_functions=createfunctions()
print(add_function(10,20))
print(sub_functions(10,20))

l=[add_function,34,78]
print(l[0](l[1],l[2]))#add_function(34,78)"""

#defining function is actual argument
#calling function is 

#positional argument
"""def add(x,y):
    return x+y
print(add(10,20))
#keyword argument
def add(x,y):
    return x+y
print(sub(x=10,y=20))
print(sub(y=20,x=10))"""

#whenever you define argument use keyword argument not positional argument

#default argument
"""def simpleinterest(p,r=2.5,t=1):
    return(p*r*t)/100
print(simpleinterest(1000))
print(simpleinterest(1000,3.5))
print(simpleinterest(1000,3.5,2))"""

#variable length argument(for positional arguments)
"""def sum(x,*y): #'*' before y means it is a tuple and can take variable length argument
    print(type(y))
    total=x
    for i in y:
        total+=i
    return total
print(sum(10,20))
print(sum(10,20,30,40,50))
print(sum(10,20,30,40,50,60,70,80,90,100))
print(sum(10))"""#tuple can be empty(error will be when u don't pass anything)

"""def sum(*y): #'*' before y means it is a tuple and can take variable length argument
    print(type(y))
    total=0
    for i in y:
        total+=i
    return total
print(sum(10,20))
print(sum(10,20,30,40,50))
print(sum(10,20,30,40,50,60,70,80,90,100))
print(sum(10))#tuple can be empty(error will be when u don't pass anything)
print(sum())"""

#keyword variable length argument(for keyword argument)
"""def printdata(**data): # '**' before data means it is a dictionary and can take variable length keyword argument
    print(type(data))
    for key,value in data.items():
        print(key,"=",value)

printdata(name="Amit",age=25,city="Delhi")
printdata(id=101,dept="IT",salary=50000,location="Noida")
printdata(a=10,b=20,c=30,d=40,e=50,f=60,g=70,h=80,i=90,j=100)"""

#local variables in python
"""def m():
    a=11
    print(a)
m()"""

"""def m():
    a=11
    print(a)
def n():
    print(a)
m()
n()"""#we got name error

"""sum=10
l=[1,2,3,4,5,6,7,8,9]
print(sum(l))"""#we are getting type error

"""def add(x,y):
    return x+y
def add(x,y,z):
    return x+y+z
def add(x,y,z,w):
    return x+y+z+w
print(add(12,56))"""

#global variables
"""a=11
b=12
def m():
    print("a from function m(): ",a)
    print("b from function m(): ",b)
def n():
    print("a from function n(): ",a)
    print("b from function n(): ",b)
m()
n()"""

"""a=1
def m1():
    a=2
    print("a value from m1() function: ",a)#here a is local so a=2
def m2():
    print("a value from m2() function: ",a)#here a is global so a=1
m1()
m2()"""

"""a=1
def m1():
    global a
    a=2
    print("a value from m1() function: ",a)#here both are global
def m2():
    print("a value from m2() function: ",a)
m1()
m2()"""

#globals built-in function in python
"""a=1
def m():
    a=2
    print(a)
    print(globals()["a"])
m()"""

"""x=1
while(x<=10): #1...10
    print(x)
    x+=1""" #this is true condition

"""x=1
while(x==11):
    print(x)
    x+=1"""

#forward tracking
"""def printdata(x):
    if x==11:
        return
    else:
        print(x)
        printdata(x+1)
printdata(1)"""

#backward tracking
"""def printdata(x):
    if x==11:
        return
    else:
        printdata(x+1)
        print(x)
printdata(1)"""

#above processes is known as recursive function.Every recursive statement is if-else statement.