import requests
import json

respuesta = requests.get('http://localhost/ej1/conecta.php')
result = respuesta.json()

print(json.dumps(result, indent=4))
