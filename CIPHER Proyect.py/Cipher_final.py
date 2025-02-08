
def caesar(original_text, shift_value, direction):
    encrypt_text = ""
    
    if direction == "decode":
        shift_value *= -1

    for character in original_text:

        if character not in alphabet:
            encrypt_text += character
        
        else:
            value_list_1 = alphabet.index(character) + shift_value
            value_list_1 %= len(alphabet)
            encrypt_text += alphabet[value_list_1]

    print(encrypt_text)

move_on = True
while move_on:

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction_2 = str(input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")).lower()
    text = input("Type your mesage: \n").lower()
    shift = int(input("Type the shift number: \n"))

    caesar(original_text = text, shift_value = shift, direction = direction_2)

    next_step = str(input("Type 'yes' if you want to continue otherwise type 'no': ")).lower()
    if next_step == "yes":
        move_on = True
    else:
        move_on = False
        print("Good bye!")