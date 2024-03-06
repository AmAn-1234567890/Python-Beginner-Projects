#TREASURE ISLAND
a1=input('Welcome to Treasure Island.\nYour mission is to find the treasure.\nYou are at the cross road.Where do you want to go?Type"Left" or "Right"\n')
a2=a1.lower()
if a2=="left":
 b1=input('You have come to a lake.There is an island in the middle of the lake.Type"wait"to wait for the boat.Type "swim" to swim across\n')
 b2=b1.lower()
 if b2=="wait":
  c1=input("You arrived at the island unharmed.There is a house with 3 doors.One red, one yellow and one blue.Which colour do you choose?\n")
  c2=c1.lower()
  if c2=="red":
   print("You entered a room full of fire.\nGAME OVER")
  elif c2=="blue":
    print("You entered a room of beasts.\nGAME OVER")
  else:
    print("You found the TREASURE.\n CONGRATULATIONS") 
 else:
   print("You entered into some terrible unexpected area.\nGAME OVER")
else:
  print("GAME OVER")