# TODO-1: Create a function called "encrypt()" that takes original_text and shift_amount as 2 inputs
# TODO-2: Inside the "encrypt()" function, shift each letter of the "text" forwards in the alphabet by the "shift" value
# TODO-3: Call the "encrypt()" function and pass in the user inputs. Show the message encrypted
# TODO-4: What happend if you try to shift "z" forwards by 9? Can ou fix the code?

def encrypt(original_text, shift_value):

    original_text = list(original_text)
    encrypt_text = []
    #print(len(alphabet))
    
    for character in range(0,len(original_text)):
        
        value_list_1 = (alphabet.index(original_text[character]) + shift_value)

        value_list_1 %= len(alphabet)

        encrypt_text.append(alphabet[value_list_1])

    print(f"{''.join(encrypt_text)}")


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#direction = str(input("Type 'encode' to encrypt, type 'decode' to decrypt: \n"))
text = str(input("Type your mesage: \n")).lower()
shift = int(input("Type the shift number: \n"))

encrypt(text,shift)



#PART 2

def encrypt(original_text, shift_value):

    original_text = list(original_text)
    encrypt_text = []
    
    for character in range(0,len(original_text)):
        value_list_1 = (alphabet.index(original_text[character]) + shift_value)
        value_list_1 %= len(alphabet)
        encrypt_text.append(alphabet[value_list_1])

    print(f"{''.join(encrypt_text)}")

def decrypt(original_text, shift_value):

    original_text = list(original_text)
    encrypt_text = []
    
    for character in range(0,len(original_text)): 
        value_list_1 = (alphabet.index(original_text[character]) - shift_value)
        value_list_1 %= len(alphabet)
        encrypt_text.append(alphabet[value_list_1])

    print(f"{''.join(encrypt_text)}")