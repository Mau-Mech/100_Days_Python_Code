print("===============")
print("Vacations days")
print("===============\n")
name = str(input("Plese type you name and last name please: "))
code = int(input("Please type the area code of you position: "))
time = float(input("Please type the number of years that you have in the company: "))

if code == 1:
   if time <1:
      print(name,",you do not have vacation days yet")
   if time >= 1:
      print(name,",your vacation days are 6 days")
   if time >= 2 and time <= 6:
      print(name,",your vacation days are 14 days") 
   if time >= 7:
      print(name,",your vacation days are 20 days")

elif code == 2:
   if time <1:
      print(name,",you do not have vacation days yet")
   if time >= 1:
      print(name,",your vacation days are 7 days")
   if time >= 2 and time <= 6:
      print(name,",your vacation days are 15 days") 
   if time >= 7:
      print(name,",your vacation days are 22 days")

elif code == 3:
   if time <1:
      print(name,",you do not have vacation days yet")
   if time >= 1:
      print(name,",your vacation days are 10 days")
   if time >= 2 and time <= 6:
      print(name,",your vacation days are 20 days") 
   if time >= 7:
      print(name,",your vacation days are 30 days")

else: 
 print("The number of the position do not exist, please try again")
print("End.")
