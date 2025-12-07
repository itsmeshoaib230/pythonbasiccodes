
print("welcome to pizza delivery!")
size=input("select the size you want S,M,L:")
pep=input("do you want pepper? yes or no:")
che=input("do you want to add cheese?yes or no:")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("please selecet available size")
if pep=="yes":
    if size=="S":
        bill+=2
    else:
        bill+=3
if che=="yes":
    bill+=1
print("your total is:")
print(bill)
        
