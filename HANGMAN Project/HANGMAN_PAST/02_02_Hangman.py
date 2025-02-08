import random
word_list=["ardvark", "baboon", "camel"]
#Testing code
chosen_word = random.choice(word_list)
print(f"The choseen word is: {chosen_word}")


#TODO 1: Create an empty List called display. 
#For each letter in the chosen_word, add a "_" to displa

#TODO 2: Loop through each position in the chosen word
#If the letter at that position matches "guess" then reveal that letter in the display at that position
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_","p","p","_","_"].
display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"
print(display)

conta = 0 

while conta < 4:
    guess = str(input("Guess a letter: ")).lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(len(display))
    print(display)
    conta += 1