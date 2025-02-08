#Secuencia con lista sin parametro list
sequence = ["uno","dos","tres"]
dic_name = dict.fromkeys(sequence)
print(f"The values of the new dictionary using only a sequence: {dic_name}")


#Secuencia con lista y parametro value y sequence
sequence = ["uno","dos","tres"]
value = 5
dic_name = dict.fromkeys(sequence,value)
print(f"The values of the new dictionary with parameters sequence and values: {dic_name}")


#Secuencia con diccionario y parametro value y sequence
sequence = {"uno": 1,
            "dos":2,
            "tres":3
            }
value = 5
dic_name = dict.fromkeys(sequence,value)
print(f"The values of the new dictionary using a dictionary as a sequence: {dic_name}")


#Secuencia con string
sequence = "Mauricio"
value = 1
dic_name = {}.fromkeys(sequence,value)
print(f"The values of the new dictionary using a string as a sequence: {dic_name}")


#Usando los parametros de manera directa
dic_name = {}.fromkeys("hola",[1,2,"Hola"])
print(f"The values of the new dictionary using directly the parameters: {dic_name}")


dic_name = {}.fromkeys("hola",{"Juan":25,"Maria":22})
print(f"TThe values of the new dictionary using directly the parameters: {dic_name}")