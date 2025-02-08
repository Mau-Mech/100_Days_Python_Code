import random
word_list=["ardvark", "baboon", "camel","apple"]
#Testing code
chosen_word = random.choice(word_list)
print(f"The choseen word is: {chosen_word}")


#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed
#  all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.


display = []

for index in range(len(chosen_word)):
    display += "_"
#print(display)

end_of_game = False
while not end_of_game: 
    #print(bool(display.index("_")))  
    guess = str(input("Guess a letter: ")).lower()
    for index in range(len(chosen_word)):
        if guess == chosen_word[index]:
            display[index] = guess
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")


