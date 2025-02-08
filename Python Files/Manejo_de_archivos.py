import json

datos_JSON = 
{
    "tamaño": "mediana",
    "precio": 15.67,
    "topping": ["champinones","queso extra","peperoni","albahaca"],
    "cliente":{
        "nombre": "Jane Doe",
        "telefono": "455-344-234",
        "correo": "joedoe@email.com"
    }

}


datos_diccionario = json.loads(datos_JSON)
print(datos_diccionario)

print(list(datos_diccionario.values()))
