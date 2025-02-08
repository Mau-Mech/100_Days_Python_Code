dict_name = {"Apple":2,
             "Banana":3,
             "Orange":4
            }
print(f"The value return of ('banana', 4) is: {dict_name.setdefault('Banana',4)} ")
print(f"The updated value of the set is : {dict_name}")
print()

print(f"The value return of ('kiwi') is: {dict_name.setdefault('kiwi')} ")
print(f"The updated value of the set is : {dict_name}")

print(f"The value return of ('mango', 4) is: {dict_name.setdefault('Mango',5)} ")
print(f"The updated value of the set is : {dict_name}")