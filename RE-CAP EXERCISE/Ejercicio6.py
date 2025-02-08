phrase =str(input("Introduce any phrase: "))
word =str(input("Type the word that you want to erase: "))
index = phrase.find(word)

new_phrase = phrase[0:index] + phrase[index+len(word)+1: len(phrase)]


print(new_phrase)