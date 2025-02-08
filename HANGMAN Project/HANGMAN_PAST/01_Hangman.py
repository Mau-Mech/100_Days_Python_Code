import random

word_list=["ardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0,len(word_list)-1)]
#print(chosen_word)

guess = str(input("Guess a letter: "))
guess=guess.lower()

#print(guess)

chosen_word = list(chosen_word)
for index in chosen_word:
    if guess == index:
        print("Rigth")
    else:
        print("Wrong")