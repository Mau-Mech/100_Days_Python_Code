# TODO-1: Create a function called "decrypt()" that takes "original_text" and "shift_value" as inputs
# TODO-2: Inside the "decript()" function, shift each letter of the original text *backwards* in the alphabet
# by the shift amount and print the decrypted text.                  
# TODO-3: Combine the "encrypt()" and "decrypt()" functions into one function called "caesar()"
# Use the value of the user chosen "direction" variable to determine which functionality to use.

def caesar(original_text, shift_value, direction):
    original_text = list(original_text)
    encrypt_text = []
    
    for character in range(0,len(original_text)):
        if direction == "decode":
            shift_value *= -1

        value_list_1 = (alphabet.index(original_text[character]) + shift_value)
        value_list_1 %= len(alphabet)
        encrypt_text.append(alphabet[value_list_1])

    value = ''.join(encrypt_text)
    print(f"Your {direction} message its: {value}")


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction_2 = str(input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")).lower()
text = input("Type your mesage: \n").lower()
shift = int(input("Type the shift number: \n"))

caesar(original_text = text, shift_value = shift, direction = direction_2)