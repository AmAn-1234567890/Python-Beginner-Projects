rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
a=int(input("What do you want to choose?Type 0 for ROCK, 1 for PAPER and 2 for SCISSOR\n"))
if a>=0 and a<3:
 if a==0:
  print(rock)
 elif a==1:
  print(paper)
 elif a==2:
  print(scissors)
 b=random.randint(0,2)
 if b==0:
  print("Computer chose\n"+rock)
 elif b==1:
  print("Computer chose\n"+paper)
 elif b==2:
  print("Computer chose\n"+scissors)
 if a==b:
  print("Try again")
 elif a==0 and b==2:
  print("You win")
 elif a==1 and b==0: 
  print("You win")
 elif a==2 and b==1:
  print("You win")
 else:
  print("You lose") 
else:
 print("Invalid number.\nYou lose")

