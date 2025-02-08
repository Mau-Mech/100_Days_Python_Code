def modificar_lista(lista):
    lista.append(4)
    print("Dentro de la funcion", lista)


mi_lista = [1,2,3]
modificar_lista(mi_lista)
print("Fuera de la funcion:", mi_lista)