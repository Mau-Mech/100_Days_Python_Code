secret_word = "chupacabra"
word = str(input("Hi, please type a world if you guess the secret one you will be out of this loop: "))
while secret_word != word:
    word = str(input("That is not the secret word try again: "))
    
print("You've successfully left the loop.")