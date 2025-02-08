import random

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list=["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = str(input("Guess a letter: ")).lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#chosen_word = list(chosen_word)
for index in chosen_word:
    if guess == index:
        print("Rigth")
    else:
        print("Wrong")