import json

Base_De_Datos = []

for elemento in range(0,3):
    persona = {}
    nombre = input("Nombre de la persona: ")
    edad = input("Edad de la persona: ")
    persona ["Nombre"] = nombre
    persona ["Edad"] = edad
    Base_De_Datos.append(persona)

print(Base_De_Datos)

with open("Base_de_datos.json","w"):
