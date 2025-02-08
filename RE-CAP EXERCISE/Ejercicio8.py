value = int(input("What value do you want to create the multiplication guide: "))

print("The result its:")
for row in range(0,11):
    print(f"{value} X {row} = {value*row}")
