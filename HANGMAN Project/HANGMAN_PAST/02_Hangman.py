import random
word_list=["ardvark", "baboon", "camel"]
#Testing code
chosen_word = random.choice(word_list)
print(f"The choseen word is: {chosen_word}")

guess = str(input("Guess a letter: ")).lower()

#TODO 1: Create an empty List called display. 
#For each letter in the chosen_word, add a "_" to display
display = []

#TODO 2: Loop through each position in the chosen word
#If the letter at that position matches "guess" then reveal that letter in the display at that position
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_","p","p","_","_"].
display = []
for index in chosen_word:
    if guess == index:
        display.append(guess)
    else:
        display.append("_")
print(display)
