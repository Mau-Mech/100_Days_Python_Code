import re
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
#PRIMERA FORMA
print("manzanas" in fruits)

#SEGUNDA FORMA 
if "manzanas" in fruits:
    print("True")
else:
    print("False")