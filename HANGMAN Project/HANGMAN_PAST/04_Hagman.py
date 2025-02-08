import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list=["ardvark", "baboon", "camel","apple"]
#Testing code
chosen_word = random.choice(word_list)
print(f"The choseen word is: {chosen_word}")
display = []
#Create the blanck spaces
for index in range(len(chosen_word)):
    display += "_"

lives = 6
end_of_game = False

while not end_of_game: 

    guess = str(input("Guess a letter: ")).lower()
    for index in range(len(chosen_word)):
        if guess == chosen_word[index]:
            display[index] = guess

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You Lose")
        

    print(display)


    if "_" not in display:
        end_of_game = True
        print("You Win!")

    if lives == 0:
        end_of_game = True
        print("You lose!")



#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.