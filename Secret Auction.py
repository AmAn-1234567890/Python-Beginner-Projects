from replit import clear
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the Secret Auction Program\n")
c="yes"
a={}
while c=="yes":
    name=input("What's your name?\n")
    price=int(input("What's your bid? \nRs."))
    a[name]=price
    c=input("Are there any bidders?\n").lower()
    clear()      
x=[]
y=[]
for i in a:
    x.append(i)
    y.append(a[i])
bidder_name=""
result=0
for i in y:
    if i>result:
        result=i
z=y.index(result)
bidder_name=x[z]
                  
print(f"The winner is {bidder_name} with a bid of Rs.{result}")