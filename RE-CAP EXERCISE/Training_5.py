#FUNCION ADIVINA EL NUMERO

import random

machine = random.randint(1,10)

executions = 0
while True:
    user = int(input("Type your number and try: "))
    executions += 1
    if machine > user:
        print("The value that you type its lower than the machine, try again")
    elif machine < user :
        print("The value that you type its higher than the machine, try again")
    else:
        print(f"The values are the same, well done!, it took you only {executions} times.")    
        break
