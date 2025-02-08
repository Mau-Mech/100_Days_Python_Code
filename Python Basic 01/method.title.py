name = input("Please type your first name: ")
last_name = input("Please type your last name: ")
full_name = f"{name} {last_name}"
print()
print(f"The format of the method title has been aplied?: {full_name.istitle()}")
print(f"The method title() is: {full_name.title()}")
print(f"This is the name of the variable: {full_name}")

print()
full_name= full_name.title()
print(f"The format of the method title has been aplied?: {full_name.istitle()}")
print(f"This is the name of the variable in permanet way: {full_name}")