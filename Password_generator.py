import random

letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols= ['!','#','$','%','&','(',')','*','+']
numbers= ['1','2','3','4','5','6','7','8','9']

print("Welcome to the PyPasword Generator!")

nr_letters = int(input(f"How Many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like \n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for l in range(nr_letters):
    password.append(letters[random.randint(0,len(letters)-1)])

for s in range(nr_symbols):
    password.append(symbols[random.randint(0,len(symbols)-1)])

for n in range(nr_numbers):
    password.append(numbers[random.randint(0,len(numbers)-1)])
    

#hard level
random_pasword = []

for randm2 in range(len(password)):
    temp = random.randint(0,len(password)-1)
    random_pasword.append(password[temp])
    del password[temp]

new_password = ""
for list in range(len(random_pasword)): 
    new_password += random_pasword[list]

print(f"Your password its: {new_password}") 
    

