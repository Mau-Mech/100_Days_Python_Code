year = int(input("Type the year that you want to know if its Normal Year or Lap year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("This is a leap year.")
else:
    print("This is a regular year.")
