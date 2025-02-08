def price (n1,n2,n3):
    res = (n1/n2)+((n1/n2)*(n3/100)) 
    return res

print("Welcome to the tip calculator")

total = float(input("What was the total bill?: "))
people = int(input("How many people to split the bill?: "))
tip = float(input("What percentage tip would you like to give 10, 15 20 or other?"))


if tip == 10:
    pay = price(total,people,tip)
    print(f"Each person should pay: {round(pay,2)}")

elif tip == 15:
    pay = price(total,people,tip)
    print(f"Each person should pay: {round(pay,2)}")
elif tip == 20:
    pay = price(total,people,tip)
    print(f"Each person should pay: {round(pay,2)}")
else:
    pay = price(total,people,tip)
    print(f"Each person should pay: {round(pay,2)}")
