print("Ejercicio #1")
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
         }

print(fruits)
number_of_manzanas = fruits.get("manzanas")

print(f"Cantidad de manzanas con el metodo get: {number_of_manzanas}")
print(f"Cantidad de manzanas consultando el valor: {fruits['manzanas']}")