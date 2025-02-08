print("The Love Calculator is calculating your score...")
name1 = "David Beckham" #str(input("What is your name?"))
name2 = "Victoria Beckham" #str(input("What is their name?"))

name1 = name1.lower()
name2 = name2.lower()
final = name1+name2

for character in name1:
    quanty1 = final.count("t")
    quanty2 = final.count("r")
    quanty3 = final.count("u")
    quanty4 = final.count("e")
    quanty5 = final.count("l")
    quanty6 = final.count("o")
    quanty7 = final.count("v")
    quanty8 = final.count("e")
final1 = quanty1 + quanty2 + quanty3 + quanty4
final2 = quanty5 + quanty6 + quanty7 + quanty8
total = str(final1)+str(final2)

if int(total)>40 and int(total)<50:
    print(f"Your score is {total}, you are alright together.")
elif int(total) < 10 or int(total) > 90:
    print(f'Your score is {total}, you go together like coke and mentos.')
else:
    print(f"Your score is {total}.")