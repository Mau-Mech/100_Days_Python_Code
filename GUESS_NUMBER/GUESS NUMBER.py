from imagen import logo
import random
print(logo)
print("Welcome to the Number Guesing Game!")
print("I'm thinking of a number between 1 and 100.")

chances = input("Choose a difficulty. Type 'easy' or 'hard'.: ")
chances.lower()
#print(chances)
if chances == "hard":
    opportunities = 5
else:
    opportunities = 10

number = random.randint(1,100)
#print(number)
#print(opportunities)

while opportunities > 0:
    opportunities -= 1
    user_value = int(input("Type your number: "))
    if opportunities == 0:
        print("You lose!")
    elif number == user_value:
        print("You win")
        break
    else:
        if user_value > number:
            print("Too high")    
            print(f"You have {opportunities} attempts remaining to guess the number.")
        if user_value < number:
            print("Too low")    
            print(f"You have {opportunities} attempts remaining to guess the number.")