#Tip Calculator
a=input("Welcome to Tip Calculator!\nWhat was the total bill? Rs.")
b=input("What is the percentage tip you want to give? ")
c=input("Number of people to split the bill? ")
d=float(a)
e=int(b)
f=int(c)
g=d*e/100
g+=d
final=round(g/f,2)
print(f"Each person would have to pay Rs.{final}")