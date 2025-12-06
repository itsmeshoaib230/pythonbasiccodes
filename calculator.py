# basic calculator program
a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
c=input("enter the operation you want to perform")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
else:
    print(a/b)