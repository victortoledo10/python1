import requests
import json


"""
print("HOlaaaa ....... ")


# Reemplaza TU_CLAVE_DE_API con tu clave de API de Football-Data
api_key = "TU_CLAVE_DE_API"

# Especifica el ID del partido que quieres consultar
match_id = 12345

# Envía una solicitud a la API para obtener información sobre el partido
response = requests.get(f"https://api.football-data.org/v2/matches/{match_id}", headers={"X-Auth-Token": api_key})

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
  # Carga la respuesta en formato JSON
  match_data = response.json()
  # Imprime información sobre el partido
  print(f"Equipo local: {match_data['homeTeam']['name']}")
  print(f"Equipo visitante: {match_data['awayTeam']['name']}")
  print(f"Resultado: {match_data['score']['fullTime']['homeTeam']} - {match_data['score']['fullTime']['awayTeam']}")
else:
  # Si la solicitud no fue exitosa, imprime el código de error y el mensaje de error
  print(f"Error {response.status_code}: {response.text}")


"""

url = "https://airport-info.p.rapidapi.com/airport"

querystring = {"iata":"MAD"}

headers = {
	"X-RapidAPI-Key": "83019c5aa1msh5cf94ba9cb01759p1d889bjsn57072312e12f",
	"X-RapidAPI-Host": "airport-info.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)


data = json.loads( response.text )


print(data)


#print(response.text)