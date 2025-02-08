dictionary_empty = {}
#Dictionary homogeneus

print(f"Dictionary empty {dictionary_empty}")
print()
dictionary_ages = {"Mauricio":28,
                   "Luis":30, 
                   "Fernanda":25, 
                   "Gael":6
                  }
print(f"Dictionary {dictionary_ages}")
print()
#Dictionary heterogeneus
dictionary_dates ={"name": "Pedro",
                   "last_name": "Arango",
                   "age": 59
                   }
print(f"Dictionary {dictionary_dates}")
print()
#Dictionary with list and dictionaries
dictionary_list = {"a":{"a":1},
                   "b":[0,1,2]
                   }
print(f"Dictionary {dictionary_list}")
print()

#Dictionary with numeric keys
dictionary_keys_num ={4:1,
                      5:2,
                      6:3
                      }

print(f"Dictionary {dictionary_keys_num}")
print()

#Dictionary with repeated keys
dictionary_repeated_keys= {"Juan":20,
                           "Gerardo":30,
                           "Juan":15
                           }

print(f"Dictionary {dictionary_repeated_keys}")
print()

#dictionary with mix tipe of data in keys
dictionary = {1:23,
              "Juan": 5,
              -2: "hola"
              }
print(f"Dictionary {dictionary}")
print()