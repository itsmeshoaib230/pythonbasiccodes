x=int(input("enter a number:"))
if x>1:
    for i in range(2,x):
        if x%i==0:
            print("not a prime")
            break
        
    else:
        print("prime number")
        