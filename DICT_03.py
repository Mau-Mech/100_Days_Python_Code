fruits = {"Piña": 5,
          "Uva": 45,
          "Platano": 8,
          "Manzanas":13,
          "Guayaba":10,
          "Durazno":12  
}


for num_2 in fruits:
    print(f"Este es el valor del contador del ciclo (key): {num_2}")
    print(f"Este es el valor del diccionario usando el contador del ciclo como indice (value): {fruits[num_2]}")