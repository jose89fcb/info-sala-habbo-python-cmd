import requests

response = requests.get("https://images.habbo.com/habbo-web-leaderboards/hhes/visited-rooms/daily/latest.json")

data = response.json()


for habbo in data:
    print("____")
    print("Nombre Dueño: " + habbo["ownerName"])
    
    print("\n\n\n")
    print("Nombre sala: " + habbo['name'])
    print("\n\n\n")
    print("Descripcion sala: " + habbo['description'])
    print("\n\n\n")
    print("La sala está: " + habbo['doorMode'])
    print("\n\n\n")
    print("Mini imagen sala: " + habbo['thumbnailUrl'])


