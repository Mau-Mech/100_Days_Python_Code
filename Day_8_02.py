def life_in_weeks(age):
    remaining = (90*52)-(age*52)
    print(f"You have {remaining} weeks left.")
    
a = int(input("¿What its your actual age ?"))
life_in_weeks(a)