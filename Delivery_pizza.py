print("Thank you for choosing Python Pizza Deliveries!")
size = str(input("What size pizza do you want? [S] ,[M] or [L]: "))
add_pepperoni = str(input("Do you want pepperoni? [Y] or [N]: "))
add_cheese = str(input("Do you want extra chese [Y] or [N]: "))

size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = add_cheese.upper()

if size == "S" and add_pepperoni == "Y" and extra_cheese == "Y":
    price = 15 + 2 + 1
    print(f"Your final bill is: ${price}")
elif size == "S" and add_pepperoni == "N" and extra_cheese == "Y":
    price = 15 + 1
    print(f"Your final bill is: ${price}")
elif size == "S" and add_pepperoni == "N" and extra_cheese == "N":
    price = 15
    print(f"Your final bill is: ${price}")
elif size == "S" and add_pepperoni == "Y" and extra_cheese == "N":
    price = 15 + 2
    print(f"Your final bill is: ${price}")
elif size == "M" and add_pepperoni == "Y" and extra_cheese == "Y":
    price = 20 + 3 + 1
    print(f"Your final bill is: ${price}")
elif size == "M" and add_pepperoni == "N" and extra_cheese == "Y":
    price = 20 + 1
    print(f"Your final bill is: ${price}")
elif size == "M" and add_pepperoni == "N" and extra_cheese == "N":
    price = 20
    print(f"Your final bill is: ${price}")
elif size == "M" and add_pepperoni == "Y" and add_cheese == "N":
    price = 20 + 3
    print(f"Your final bill is: ${price}")
elif size == "L" and add_pepperoni == "Y" and extra_cheese == "Y":
    price = 25 + 3 + 1
    print(f"Your final bill is: ${price}")
elif size == "L" and add_pepperoni == "N" and add_cheese == "Y":
    price = 25 + 1
    print(f"Your final bill is: ${price}")
elif size == "L" and add_pepperoni == "N" and extra_cheese == "N":
    price = 25
    print(f"Your final bill is: ${price}")
elif size == "L" and add_pepperoni == "Y" and extra_cheese == "N":
    price = 25 + 3
    print(f"Your final bill is: ${price}")
else:
    print("The option that you choose does not exist in the menu")