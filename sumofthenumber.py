x=int(input("enter the number:"))
rem=0
while x!=0:
    rem+=x%10
    x=x//10
print("tne sum of the given number:")
print(rem)