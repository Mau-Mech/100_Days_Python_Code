fichero = open('./My_first.txt', 'rt', encoding = 'utf-8')
# r = read
#w = write i existe ese fichero y lo va a sobreescribir y elimina la info
#a = append
#x = create

# t = text-mode
# b =bytes - para archivos como fotos

primeraLinea = fichero.readline()  #Este metodo te lee la primera linea
print(primeraLinea)
print(fichero.readline()) #Este metodeo lee la siguiente linea
print(fichero.readline())