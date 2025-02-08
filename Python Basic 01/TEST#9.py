phrase = input("Please type any phrase: ")
end_loop_code = input("¿With what letter do you want to end the loop?: ")
new_phrase = ""
#delete all the vowels

for new_phrase in phrase:
    if new_phrase.lower() == end_loop_code.lower():
       break
    elif new_phrase.upper() == end_loop_code.upper():
       break
    elif new_phrase == "a" or new_phrase == "e" or new_phrase == "i" or new_phrase == "o" or new_phrase == "u":
     continue
    print (new_phrase, end ="")