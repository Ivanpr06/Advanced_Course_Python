import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

respuesta = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
#print(respuesta.json())
print(json.dumps(respuesta.json()))