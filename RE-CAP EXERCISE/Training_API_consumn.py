#Consume una API para obtener la frase del dia

import requests

URL = "https://frasedeldia.azurewebsites.net/api/phrase"

response = requests.get(URL)
data = response.json()

print(data)
print(data["phrase"])
