# COMPROBAR SI UNA FRASE ES UN PALINDROMO SIN TOMAR EN CUENTA ESPACIOS MAYUSCULAS NI TILDES

def palindromo (phrase):

    minus_phase = phrase.lower()
    long_string = minus_phase.strip()
    long_string = long_string.replace("á","a")
    long_string = long_string.replace("é","e")
    long_string = long_string.replace("í","i")
    long_string = long_string.replace("ó","o")
    long_string = long_string.replace("ú","u")
    inverse = long_string[::-1]
    for i in range(len(long_string)):
        if inverse[i] != long_string[i]: 
            return False
        else:
            return True


string = str(input("Please type the phase: "))
check = palindromo(string)


if check:
    print("The phrase is a palindrome")
else: 
    print("The phrase is NOT a palindrome")
