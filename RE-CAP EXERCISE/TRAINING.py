def serie(val1):

    list = []
    for num in range(1 , val1 + 1):
        list.append(num)
        #print(list, end= ",")
    print("\n")
    print(list)
    sum = ((val1+1)*(val1))/2
    print(f"El valor de la suma es: {int(sum)}")

    for i in list:
        print(i, end = " ")



valor = int(input("Fin de la serie a sumar: "))

serie(valor)