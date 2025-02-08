def calculation(number_1,number_2,choose):
    if choose == "+":
        return number_1 + number_2
    elif choose == "-":
        number_3 = number_1 - number_2
        return number_3
    elif choose == "*":
        number_3 = number_1 * number_2
        return number_3
    elif choose == "/":
        number_3 = round(number_1 / number_2,2)
        return number_3
    

num1 = float(input("What's the first number?: "))
loop_number = True
temp_num1 = num1
while loop_number == True:
    print("+ \n- \n* \n/")
    option = str(input("Pick an operation: "))
    num2 = float(input("What's the next number?: "))
    num3 = calculation(number_1=temp_num1,number_2=num2,choose=option)
    temp_num1 = num3 
    print(temp_num1)
    print(f"{temp_num1}{option}{num2} = {num3}") #entender bien esta linea, revisalo
    next_calculation = str(input(f"Type 'y' to continue calculating with {num3} , or type 'n' to start new calculation: ")) 
    print(next_calculation)
    if next_calculation == "y":
        print(temp_num1)
        print(num3)
    else: 
        next_calculation == "n"
        print(loop_number)
        loop_number = False
        print(loop_number)
        #break #Porque no funciona sin esto?