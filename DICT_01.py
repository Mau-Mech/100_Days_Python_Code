vencedores_copas = {1990: 'Alemania', 
                    1994: 'Brasil', 
                    1998: 'Francia', 
                    2002: 'Brasil', 
                    2006: 'Itália', 
                    2010: 'Espana', 
                    2014: 'Alemania', 
                    2018: 'Francia'}


#print(vencedores_copas[2018])
#print(vencedores_copas.values())
#print(vencedores_copas.keys(1))
#print(vencedores_copas.items())

for index_1 in vencedores_copas:
    if vencedores_copas[index_1] == "Alemania":
        print(vencedores_copas[index_1])

print("\n")

#for index_1, index_2 in vencedores_copas.items():
#   print(f"este es el index 1: {index_1}")
#   print(f"este es el index 2: {index_2}")

