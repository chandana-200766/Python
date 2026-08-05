a=int(input("enter a number:"))
if a>0:
    print("number is positive")
elif a<0:
    print("number is negative")
else:
    print("number is zero")


#2.program
b=int(input("enter b number:"))
if b%2 ==0:
    print("number is even")
else:
    print("number is odd")


#3.program
c=int(input("enter c number:"))
if c>18:
    print("eleigible for vote")
else:
    print("not eleigible for vote")


#4.program
marks=int(input("enter marks:"))
if marks>=35:
    print("pass")
else:
    print("fail")


#5.program
score=int(input("enter a marks:"))
if score>=90 and score<=100:
    print("Grade A")
elif score>=75:
    print("Grade B")
elif score>=60:
    print("Grade C")
elif score>=35:
    print("Grade D")
elif score>=0:
    print("Fail")
else:
    print("invalid marks")


#6.program
e=int(input("give value:"))
f=int(input("give another value:"))
if e>f:
    print("e is largest value",e)
else:
    print("f is largest value",f)    



#7.program
v=int(input("enter first number:"))
g=int(input("enter a second number:"))
h=int(input("enter a third number:"))
if v>=g and v>=h:
    print("v is largest number",v)
elif g>=v and g>h:
    print("g is largest number",g)
else:
    print("h is largest number",h)
