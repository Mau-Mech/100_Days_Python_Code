dictionary = {"Mauricio": 28,
              "Luis": 30,
              "Fernanda": 25,
              "Gael": 6,
              "Pedro": 59,
              "Patricia": 56,
              "Romina": 0,
              "Omar": 32
              }

print("PRIMERA MANERA")
for key in dictionary:
    print(f"This are the keys: {key}", end =" ")
    print(f"This are the values: {dictionary[key]}")

print("SEGUNDA MANERA")
for key,value in dictionary.items():
    print(f"{key} : {value}")