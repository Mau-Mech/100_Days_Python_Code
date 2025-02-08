dictionary ={"a":1,
             "b":2,
             "c":3
             }

print(f"Original dictionary is: {dictionary}")

dictionary.update({'z':4,'d':5})
print(f"Adding the elements 'z' and 'd': {dictionary}")

dictionary.update({'a':6,'b':5})
print(f"Updating the elements 'a' and 'b': {dictionary}")
