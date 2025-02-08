# PROGRAMA QUE VALIDA SI UNA CONTRASEÑA ES SEGURA:
#DEBE CONTENER:
#MAS DE 8 CARACTERES
#TIENE ALMENOS UNA LETRA MAYUSCULA
#TIENE ALMENOS UN NUMERO

def password_check (password):
    largo = False
    mayus = False
    numer = False
    if len(password) > 8:
        largo = True
    for i in range(len(password)):
        if password[i].isupper():
            mayus = True
        if password[i].isnumeric():
            numer = True
    if largo and mayus and numer: #Esta linea da por entendido que el valor es "True"
        return True
    else: #Esta linea da por entendido que el valor es "False"
        return False

password_1 = str(input("Please type the password: "))
verification = password_check(password_1)

if verification:
    print("The password is secure")
else: 
    print("The password is NOT secure")