#recursive function
#if says how to stop and else says how to continue
"""def sumofdigits(number):
    if number=="":
        return 0
    else:
        return int(number[0])+sumofdigits(number[1:])
print(sumofdigits("12345"))"""

#function pe sod use hoga
#sod is sum of digits(calculated by repeatedly adding its last digit to sum of remaining digits)
"""def sod(num):
    pass
print(sod(12345))"""#q=num//10, r=num%10

"""def sod(num):
    if num==0:
        return 0
    else:
        return (num%10) + sod(num//10)
print(sod(12345))"""

#this is referred to as returning the modified function
"""def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
print(power(2,3))"""

"""def sod(num,s):
    if num==0:
        return s
    else:
        return sod(num//10,s+(num%10))
print(sod(12345,0))"""

#strrev is reverse string
"""def strrev(str,rev):
    if str=="":
        return rev
    else:
        return strrev(str[1:], str[0]+ rev)
print(strrev("Yes",""))"""

#palindrome is a word,string or number that reads forward and backward
#jo kaam loop se hote hain wo sab recurse se hote hain and recursive gives benefit for smaller codes
"""def ispalindrome(str,end,start):
    if start==end:
        return True
    elif str[start]!=str[-(start+1)]:
        return False
    else:
        return ispalindrome(str,end,start+1)
print(ispalindrome("Raj",len("Raj"),0))"""

#factorial using recursive function in python
"""def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result
x = factorial(4)
print("Factorial of 4 is:",x)"""

#lambda function in python
"""s = lambda a: a*a
x = s(4)
print(x)

add = lambda a, b : a+b
x = add(4,5)
print(x)"""

#map is a generator function, ye hmesha list ke through pass hoga
"""def cube(x):
    return x*x*x
l = [1,2,3,4,5]
l1 = list(map(cube,l))
print(l1)

l2 = list(map(lambda x: x*x*x,l))
print(l2)"""

"""num = list(map(int,input().split()))
print(num)"""

"""def cube(x):
    return x*x*x
num = list(map(cube,[int(i) for i in input().split()]))
print(num)
num1 = [cube(x) for x in [int(i) for i in input().split()]]
print(num1)
num2 = list(map(cube,list(map(int,input().split()))))
print(num2)"""

#generator function
#return means go back and yield means store the value
#mapping is something that values map of the function
"""def cube(x):
    return x*x*x
def apnamap(func,l):
    for i in l:
        yield func(i)
l = [1,2,3,4]
l2 = list(apnamap(cube,l))
print(l2)"""

#generator function use yield while normal function use return
"""def genval(start,end,step):
    while(start <= end):
        yield start
        start += step
print(list(genval(0,12,2)))"""

"""l = [1,2,3,4,5,6,7,8,9]
l1 = list(filter(lambda x: x > 6 ,l))
print(l1)"""

from functools import reduce
l = ["Python","is","Programming","language"]
longestword =  reduce(lambda x, y:x if len(x) > len(y) else y,l)
longlength = len(longestword)
print(longlength)