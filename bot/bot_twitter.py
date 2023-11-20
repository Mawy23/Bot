import gramaticas, requests, json, time
from requests_oauthlib import OAuth1

API_KEY = "j3p1B48c7EaF5o12I8KQTKQa2"
API_SECRET = "0cKWyoTCmDlDtPYDnVSCHz8ZnLpFvUtepgJ6zntJ7LJ1Jtm0R8"
ACCES_TOKEN = "1721968268322246657-n7CAy7iEBgsdp7Ka3c2ktUAAzvToQx"
ACCES_SECRET = "jxAKvA01Ezub8QPmUR79llpgcVa8uUdHc6Rz7gAq5GxkL"

# URL de la API de Twitter para publicar un tweet
url = 'https://api.twitter.com/2/tweets'

#cogemos un mensaje
data = {
    'text': gramaticas.generar_frase()
}

#imprimimos el mensaje, que va a twittear
print(f"\n{data['text']}")
time.sleep(2)

# Agregar el encabezado de tipo de contenido
headers = {
	'Content-Type': 'application/json'
}

# Configurar la autenticación OAuth1, porque sino no podemos publicar
auth = OAuth1(API_KEY, API_SECRET, ACCES_TOKEN, ACCES_SECRET)

# Realizamos la petición con el metodo POST, con los datos, la url, la autenticación y los encabezados
response = requests.post(url, auth=auth, headers=headers, data=json.dumps(data))

# Verificar la respuesta por parte del servidor
if response.status_code == 201:
    print('\n\nTweet publicado exitosamente!')