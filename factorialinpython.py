x=int(input("Enter the number:"))
ans=1
for i in range(1,x+1):
    ans*=i
print("The factorial of the number",x,"is =",ans)