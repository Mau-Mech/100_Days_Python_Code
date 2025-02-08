dictonary = {"a": 1,
             "e": 2
             }
print(dictonary)
print(f"Key a: {dictonary['a']}")
print(f"Key e: {dictonary['e']}")

print()


dictionary = {"numbers": [18, 20, 28],
              "groups": {"a": 1, "b": 2}
              }
print(dictionary)
print(f"keys numbers: {dictionary['numbers']}")
print(f"keys groups: {dictionary['groups']}")

print(f"keys numbers: {dictionary['numbers'][1]}")
print(f"keys groups: {dictionary['groups']['b']}")
print(f"keys groups: {dictionary['groups']['z']}") #Esta linea debe fallar porque no existe la clave z
