string = str(input("Type the string that you want to reverse: "))
reverse_string = ""


for character in string:
    reverse_string = character + reverse_string
    #print(character)
    #print(reverse_string)

print(f"The reverse string its: {reverse_string}")