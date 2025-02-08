phrase = input(str("Type the frase that you want to count: "))

letters = dict.fromkeys(phrase, 0)
for letter in phrase:
    letters[letter]+= 1

print(letters)