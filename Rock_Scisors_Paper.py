import random

rock = """ 
   _________
__|    _____)
      (_____) 
      (_____)        
      (_____) 
---._(_____)      
"""
paper = """ 
   ___________
__|    _______)__
      (__________) 
      (___________)        
      (__________) 
---._(________)      
"""

scissors = """ 
   _________
__|    _____)____
      (__________) 
      (___________)        
      (_____) 
---._(____)      
"""

options = [rock,paper,scissors]

value1 = int(input("What do you want to choose?, 0 for rock, 1 for paper 2 for Scissors: "))
value2 = random.randint(0,len(options)-1)


if value1 == value2:
    print(f"You choose:")
    print(options[value1])
    print("The computer choose:")
    print(options[value2])
    print("No one wins")

if value1 == 0 and value2 == 1:
    print("You choose:")
    print(options[value1])
    print("The computer choose:")
    print(options[value2])
    print("Rock its defeat by paper, the computer wins")    

if value1 == 0 and value2 == 2:
    print("You choose:")
    print(options[value1])
    print("The computer choose:")
    print(options[value2])
    print("Rock beat the Scissors, you win")

if value1 == 1 and value2 == 0:
    print("You choose:")
    print(options[value1])
    print("The computer choose:")
    print(options[value2])
    print("Rock its defeat by Paper, you win")    

if value1 == 1 and value2 == 2:
    print("You choose:")
    print(options[value1])
    print("The computer choose:")
    print(options[value2])
    print("Paper its defeat by Scissors, the computer wins")

if value1 == 2 and value2 == 0:
    print("You choose:")
    print(options[value1])
    print("The computer choose:")
    print(options[value2])
    print("Scissors are defeat by Rock, the computer wins")

if value1 == 2 and value2 == 1:
    print("You choose:")
    print(options[value1])
    print("The computer choose:")
    print(options[value2])
    print("Scissors defeat the paper, you win")

else:
    print("The option that you choose its invalid.")