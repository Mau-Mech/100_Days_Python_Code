print("Calculator practice exercise")
print("*****************")
print("*Menu of options*")
print("*****************")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Integer Division")
print("6. Power")
print("7. Module")

option = int(input("Please choose an option (Between the numbers 1 to 7)"))
#Adition
if option == 1:
   num = int(input("Plese type the first number: "))
   num += int(input("Plese type the second number: "))
   print("The resul of the Addition is: ", num)
#Substraction   
elif option == 2:
   num = int(input("Plese type the first number: "))
   num -= int(input("Plese type the second number: "))
   print("The resul of the Substraction is: ", num)
#Multiplication
elif option == 3:
   num = int(input("Plese type the first number: "))
   num *= int(input("Plese type the second number: "))
   print("The resul of the Multiplication is: ", num)
#Regular Division
elif option == 4:
   num = int(input("Plese type the first number: "))
   num /= int(input("Plese type the second number: "))
   print("The resul of the Division is: ", round(num,2))
#Integer Division
elif option == 5:
   num = int(input("Plese type the first number: "))
   num //= int(input("Plese type the second number: "))
   print("The resul of the Division without decimals is: ", num)
   #Power
elif option == 6:
   num = int(input("Plese type the first number: "))
   num **= int(input("Plese type the second number: "))
   print("The resul of the Power is: ", num)
   #Module
elif option == 7:
   num = int(input("Plese type the first number: "))
   num %= int(input("Plese type the second number: "))
   print("The resul of the Module is: ", num)
else:
   print("The option do not exist, please try again")

print("End")