import requests

# De URL van de API endpoint
url = 'https://jsonplaceholder.typicode.com/posts'

# Een GET-verzoek naar de API
response = requests.get(url)

# Controleer of het verzoek succesvol was (status code 200)
if response.status_code == 200:
    # Zet de JSON-respons om naar een Python lijst van dictionaries
    posts = response.json()
    # Print de eerste post als een voorbeeld
    print(posts[0])
else:
    print(f'Er is iets misgegaan. Status code: {response.status_code}')

# -------  API Requests -------
# Header:
# Definieer de headers voor het request. Headers bevatten metadata over het request,
# zoals content-type of authenticatie-informatie zoals een API key.

# Params:
# Stel params in voor het request als je werkt met een GET-methode.
# Params zijn query parameters die aan de URL worden toegevoegd om specifieke data op te vragen of te filteren.

# Data:
# Voeg data toe aan het request als je werkt met POST, PUT of DELETE methoden.
# Data bevat de payload die naar de server wordt gestuurd, vaak in de vorm van een JSON-object.

# nog beter is
import requests

# URL, data, headers en params gedefinieerd
url = 'https://jsonplaceholder.typicode.com/posts'
data = {'title': 'Een nieuwe post', 'body': 'Dit is de inhoud van mijn nieuwe post'}
headers = {'Content-Type': 'application/json'}
params = {'key': 'value'}  # Voorbeeld van een parameter

# Verstuur het POST-verzoek met data, headers en params
response = requests.post(url, json=data, headers=headers, params=params)

# Controleer de respons en print resultaat
if response.ok:
    print(f'Succesvol aangemaakt: {response.json()}')
else:
    print(f'Er is iets misgegaan. Status code: {response.status_code}')


# ------- Veilige API-keys -------
# .env

# Sla API keys niet hardcoded op in je code.
# - Gebruik een .env bestand#
# - Gebruik de “dotenv” library

# https://pypi.org/project/python-dotenv/

# ------- Requirements.txt -------
# Maakt een requirements.txt bestand waarin al je afhankelijkheden staan.

# Je kan dit bestand genereren met:
# Bash:
# -pip freeze > requirements.txt