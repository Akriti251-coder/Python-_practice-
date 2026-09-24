"""text=input("PROGRAMMING")
even=text[0::12]
odd=text[1:2]
print("Even positions:",even)
print("Odd positions:",odd)"""
"""string = input("Enter a string: ")
start = int(input("Enter a start index: "))
end = int(input("Enter end index: "))
substring = string[start:end]
reversed_string = substring[::-1]
print("Original string:",string)
print("Substring:",substring)
print("Reversed substring:",reversed_string)"""

"""s="PYTHONPROGRAMMING"
print("Original:",s)
print("First 3:",s[:3])
print("Last 3:",s[-3:])
print("Index 2 to 7:",s[2:8])
print("Every 2nd character:",s[::2])
print("Reversed",s[::-1])"""

"""s="Akansha"
a=s[:2]
b=s[2:5]
c=s[5:]
print(a)
print(b)
print(c)
print("Reversed:",s[::-1])
print("Reversed:",a[::-1])
print("Reversed:",b[::-1])
print("Reversed:",c[::-1])"""

"""s1="This a merged batch. We will complete string today."
print(id(s1))
c=s1.count("a")
print(c)
print(id(s1))
s1="This a merged batch. We will complete string today."
print(id(s1))
print(s1)
s1.replace("today","tomorrow")
print(s1)
print(id(s1))
s1="This a merged batch. We will complete string today."
print(id(s1))
print(s1)
s1=s1.replace("today","tomorrow")
print(s1)
print(id(s1))"""

"""message="Python programming language"
n=message.split()
print("Before splitting",message)
print("After splitting",n)
print(type(n))
for x in n:
    print(x)"""

"""s1="13:32:55"
h,m,s=s1.split(":")[0],s1.split(":")[1],s1.split(":")[2]
print(h)
print(m)
print(s)"""

"""l1=["Rajesh","Jai","Rohit","Chetan"]
s1="-".join(l1)
print(s1)
profile=["Roshan","Actor","India"]
candidate="-".join(profile)
print(profile)
print(candidate)
name="raj"
s=input("Enter fixed name")
if name==s.lower():
    print("OK")
else:
    print("not OK")
name="Rahul"
print(name.lower())
print(name.upper())
print(name.swapcase())
print(name.tile())
print(name.capitalize())"""
"""name="Rahul"
print(name.isalnum())
val=input("Enter value")
val=val if val.isalpha() else eval(val)
print(val)
print(type(val))

name="Rohit"
age="18"
place="Delhi"
#sub="{a} lives in {c} and his age is {b}".format(a=name,b=place,c=age)
sub=f"{name} lives in {place} and his age is {age}"
print(sub)

s1="ABCDEF PYTHON STRING"
s2=" "
split= s1.split()
for split in s1:
    even_chars = split[0::2]
    s2=s2+ even_chars+" "
print(s2.strip())
s1="The quick brown fox jumps over the lazy dog"
s2=s1.count("fox")
print(s2)

s1="thequickbrownfoxjumpsoverthelazydog"
s2=s1.count("t" ,"h")
print(s2)"""

"""x=int(input("Enter a number: "))
if x<0:
    print("The number is negative number")
else:
    print("The number is positive number")

user_name="rahul"
x=input("Enter a name: ")
if user_name ==x:
    print("The name is valid")
else:
    print("The name is invalid")

x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
if x>y:
    print("Biggest Number is: ",x)
else:
    print("Biggest Number is: ",y)

x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
z=int(input("Enter Third Number: "))
if x>y and x>z:
    print("Biggest Number is: ",x)"""

"""a=int(input("Enter English Number: "))
b=int(input("Enter Hindi Number: "))
c=int(input("Enter Maths Number: "))
d=int(input("Enter Science Number: "))
e=int(input("Enter Geography Number: "))
f=int(input("Enter History Number: "))
z=a+b+c+d+e+f
print(z)
x=z/6
print(x)
if x>=90 and avg<=100:
    print("Ramu received A+")
elif x>=80 and x<90:
    print("Ramu received A")"""

"""x=1
while x<=5:
    print(x)
    x+=1
print("End")

x=10
while (x>=10) and (x<=20):
    print(x)
    x+=2
print("End")
x=[10,20,30,"Python"]
for i in x:
    print(i)
x="python"
for ch in x:
    print(ch)
items_costs=[10,20,30]
gst=2
for x in items_costs:
    print(x+gst)
for x in range(1,5):
    print(x)

item_costs=[10,20,30]
sum=0
for x in item_costs:
    sum=sum+x
print(sum)

x=(input("Enter a input:"))
sum=0
for y in x:
    sum=sum+int(y)
print(sum)

for x in range(1,8):
    for x in range(x):
        print("*",end=" ")
    print()

for x in range(1,6):
    for y in range(x):
        print(x+y,end=" ")
    print()"""

"""for x in range(5,0,-1):
    for y in range(x):
        if y%2==0:
           print("#",end=" ")
        else:
            print("*",end=" ")
    print()"""

"""group = [1,2,3,4]
search = int(input("Enter the element in search: "))
for element in group:
    if search == element:
        print("element found in group")
        break

for x in range(1,500):
    if x%10==0 and x%5==0:
        continue;
    print(x)
cart = [10,20,500,700,50,60]
for item in cart:
    if item>=500:
        continue
    print("item",item)
for x in range(1,500):
    if x%10==0 and x%5==0:
        pass
    else:
        print(x)
x=1
if x<=10:
    print(x)
else:
    print("Invalid")
x=1
while x<=3:
    print("Hi")
    x+=1
else:
    print("Hello")
for x in [1,2,3,4,5]:
    print(x)
else:
    print("Completed")

while x<=3:
    print("Hi")
    x+=1
    if x==2:
        break
else:
    print("Hello")

for x in [1,2,3,4,5]:
    print(x)
    if x==4:
        break
else:
    print("Completed")

group=[1,2,3,4]
search=int(input("Enter the element in search:"))
for element in group:
    if search == element:
        print("element found in group")
        break
else:
        print("Element not found")
x=10
def sum(a,b):
    print("Sum of two values:",(a+b))
def multiplication(a,b):
    print("Multiplication of two values:",(a+b))"""
"""l1 = []
print(l1)
print(type(l1))
r=range(0,10)
l=list(r)
print(l)
names=["Mohan","Prasad","Mohan","Ramesh",10,20,True,None]
print(names)
l=[1,2,3,4,5]
print(l)
print("Before modifying l[0]:",l[0])
l[0]=20
print("After modifying l[0]:",l[0])
names=["Prabhas","Prashast","Prakash"]
print(names)
print(names[0])
print(names[1])
print(names[10])

n=[1,2,3,4,5,6]
print(n)
print(n[2:5:2])
print(n[4::2])
print(n[3:5])
a=[100,200,300,400]
for x in a:
    print(x)

a=[100,200,300,400]
x=0
while x<len(a):
    print(a[x])
    x=x+1
n=[1,2,3,4,5,5,5,3]
print(n.count(5))
print(n.count(3))
print(n.count(2))
l=[]
l.append("Ramesh")
l.append("Suresh")
l.append("Naresh")
print(l)
n=[10,20,30,40,50]
n.insert(0,76)
print(n)
l=[10,20,30,40]
print(l) 
l.insert(1,111)
print(l)
l.insert(-1,222)
print(l)
l.insert(10,333)
print(l)
l.insert(-10,444)
print(l)"""
n=[1,2,3]
n.remove(1)
print(n)