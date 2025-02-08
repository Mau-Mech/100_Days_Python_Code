dictionary_ages = {"Mauricio": 28,
                   "Luis": 30,
                   "Fernanda": 25,
                   "Gael": 6,
                   "Pedro": 59,
                   "Patricia": 56
                   }

print(f"the dictionary is: {dictionary_ages}")
print(f"\n The keys's list are:\n{dictionary_ages.keys()}")

print("\nConvertion of keys to a list using the constructor list()")
list_keys=list(dictionary_ages.keys())

print(f"The list is: {list_keys}")
print(f"The position 4 in the list is: {list_keys[3]}")