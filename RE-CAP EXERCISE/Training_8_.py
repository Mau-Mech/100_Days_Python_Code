#Funcion que devuelva el numero menor de una lista recibida por parametros 

def get_minor(list):
    min = list[0]
    for num in list:
        if min > num:
            min = num
        else:
            min = min
    return min

print(get_minor([38,15,10,100,99,1000]))
