from imagen import logo
import random

def dificulty(times):
    if times == "hard":
        opportunities = 5
        return opportunities
    else:
        opportunities = 10
        return opportunities

def guess_number(lives,computer_value):
    lives = int(lives)
    while lives > 0:
        lives -= 1
        user_value = int(input("Type your number: "))
        if lives == 0:
            print("You lose!")
        elif computer_value == user_value:
            print("You win")
            break
        else:
            if user_value > computer_value:
                print("Too high")    
                print(f"You have {lives} attempts remaining to guess the number.")
            if user_value < computer_value:
                print("Too low")    
                print(f"You have {lives} attempts remaining to guess the number.")

print(logo)
print("Welcome to the Number Guesing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)

chances = input("Choose a difficulty. Type 'easy' or 'hard'.: ")
chances.lower()

guess_number(dificulty(chances), number)