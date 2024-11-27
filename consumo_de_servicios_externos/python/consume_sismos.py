import requests
import json

respuesta = requests.get('https://api.gael.cloud/general/public/sismos')
result = respuesta.json()

print(json.dumps(result, indent=4))
