print("===============")
print("Vacations days")
print("===============\n")
print("Welcome to the vacation system, please tab enter and type the next information")
name = str(input("Please type your full name: "))
code = int(input("Please type your code: "))
time = int(input("Please time you time working (in years): "))

if code == 1 and time <= 1 :
    print(f"The employe {name} will have 6 days of vacations")
elif code == 1 and time > 1 and time <= 7:
    print(f"The employe {name} will have 14 days of vacations")
elif code == 1 and time > 7 :
    print(f"The employe {name} will have 20 days of vacations")

elif code == 2 and time <= 1 :
    print(f"The employe {name} will have 7 days of vacations")
elif code == 2 and time > 1 and time <= 7:
    print(f"The employe {name} will have 15 days of vacations")
elif code == 2 and time > 7:
    print(f"The employe {name} will have 22 days of vacations")

elif code == 3 and time <= 1 :
    print(f"The employe {name} will have 10 days of vacations")
elif code == 3 and time > 1 and time <= 7:
    print(f"The employe {name} will have 20 days of vacations")
elif code == 3 and time > 7:
    print(f"The employe {name} will have 30 days of vacations")

else:
    print("You put a wrong code please repeat: ")