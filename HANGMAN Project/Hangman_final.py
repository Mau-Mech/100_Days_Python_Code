import random
#from replit import clear
from hangman_words import word_list
from hangman_art import stages , logo

print(logo)
chosen_word = random.choice(word_list)
#Testing code
#print(f"The choseen word is: {chosen_word}")

display = []
#Create the blanck spaces
for index in range(len(chosen_word)):
    display += "_"

lives = 6
end_of_game = False

while not end_of_game: 

    guess = str(input("Guess a letter: ")).lower()
    #clear()
    if guess in display:
        print(f'The "{guess}" was already used.')      
    for index in range(len(chosen_word)):
        if guess == chosen_word[index]:
            display[index] = guess

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives > 0:
            print(f'The chosen letter "{guess}" is not in the word, try again!')

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    if lives == 0:
        end_of_game = True
        print("You lose!")