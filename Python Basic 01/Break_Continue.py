#Ejemplo de break
print("While using the sentence break \n")
count = 0
while count < 10:
    count += 1

    if count == 5:
        break
    
    print("The actual value of the variable is: ", count)
print("The program is stop due to the condition")

#Ejemplo de cntinue
print("\n While using the sentence break \n")
count = 0
while count < 10:
    count += 1

    if count == 5:
        continue
    
    print("The actual value of the variable is: ", count)