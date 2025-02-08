def add (num_1,num_2):
    return num_1 + num_2
def susbtract(num_1,num_2):
    return num_1 - num_2
def multiply(num_1,num_2):
    return num_1*num_2
def divide(num_1,num_2):
    return round(num_1/num_2,2)

operations = {
    "+": add,
    "-": susbtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    next_loop = False

    while not next_loop:
        print("+ \n- \n* \n/")
        option = str(input("Pick an operation: "))
        num2 = float(input("What's the next number?: "))

        if option in operations:
            total = operations[option] #se puede hacer esto en una sola linea, si = operations[option](num1,num2)
            num1 = total(num1,num2)

        next_calculation = str(input(f"Type 'y' to continue calculating with {num1} , or type 'n' to start new calculation: "))

        if next_calculation == "y":
            next_loop = False
        else: 
            next_loop = True
            print("\n"*20)
            calculator()


calculator()