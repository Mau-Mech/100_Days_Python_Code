math = int(input("Please type the math final note: "))
biology = int(input("Please type the biology final note: "))
chemistry = int(input("Please type the chemistry final note: "))


def final_note (math,biology,chemistry):
    final = ((math*.3) + (biology*.3)+(chemistry*.4))
    return (final)

nota = final_note(math,biology,chemistry)
print(f"The final note of the student is: {round(nota,2)}")
