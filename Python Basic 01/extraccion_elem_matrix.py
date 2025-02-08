num = int(input("how many year do you want to investigate?: "))


x = []
for colum in range (num):
    x.append(int(input("Enter a year: ")))
print(x)    

for y in x:
    if y < 1582:
	    print(f"Not within the Gregorian calendar period the year: {y}")
    elif y%4!=0 and y%400!=0:
        print(f"It's a common year:{y}")
    elif y % 100 !=0:
        print(f"It's a leap year: {y}")
    else: 
        print(f"It's a leap year: {y}")
