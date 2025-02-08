word_1 = input(str("Please type the first word or phrase: "))
word_2 = input(str("Please type the second word or phrase: "))
word_1 = word_1.lower() #Convertir todos los caracteres a minusculas
word_2 = word_2.lower()

if len(word_1) > 100 or len(word_2)>100:
    print("The length allowed its 100 or less, please try again. ")
else:
    list_1 = list(word_1) #Convertir en lista el string
    list_2 = list(word_2)
    list_1.sort() #Ordenar la lista
    list_2.sort()
    value = True #Variable de control sobre que resultado imprimir

    #Remover espacios en blanco
    for index_1 in list_1:
        if " " in list_1:
            list_1.remove(" ")
    for index_2 in list_2:
        if " " in list_2:
            list_2.remove(" ")

    #Comparar los valores de las listas
    for index_3 in range(0 , len(list_1)):
        if list_1[index_3]!=list_2[index_3]:
            value = False
            break
        else:
            value = True

    print(value) #Resultado final