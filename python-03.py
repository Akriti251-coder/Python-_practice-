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