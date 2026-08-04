num1=int(input("enter fist number:"))
num2=int(input("enter second number:"))
operator=input("enter operator:")
if operator=="+":
    print(f"ADdation of 2 numbers is:{num1+num2}")
elif operator=="-":
    print(f"Subtraction of 2 numbers is:{num1-num2}")
elif operator=="*":
    print(f"Multiplication of 2 numbers is:{num1*num2}")
elif operator=="/":
    print(f"Division of 2 numbers is:{num1/num2}")
else:
    print("not valid")
