# ------- Aantekeningen les 7 -------

# API's
# Application Programming Interface

# - OSI application laag
# - Externe gegevens of functies aan vragen
# - protocollen voor communicatie tussen software applicaties

# https://github.com/hogeschoolnovi/frontend-api-list

# ------- HTTP methodes -------
# Actie	    -   Methode
# Create    -   POST
# Read	    -   GET
# Update	-   PUT, PATCH
# Delete	-   DELETE

# ------- Uitleg -------
# POST      –   om iets nieuws aan te maken
# GET       –   om data op te halen
# PUT       –   om iets volledig bij te werken
# PATCH     –   om iets gedeeltelijk bij te werken
# DELETE    –   om iets te verwijderen

# -------  HTTP Status Codes Overzicht -------
# Level 200 (Success)
# - 200: OK
# - 201: Created
# - 203: Non-Authoritative Information
# - 204: No Content

# Level 400 (Client Errors)
# - 400: Bad Request
# - 401: Unauthorized
# - 403: Forbidden
# - 404: Not Found
# - 409: Conflict

# Level 500 (Server Errors)
# - 500: Internal Server Error
# - 501: Not Implemented
# - 502: Bad Gateway
# - 503: Service Unavailable
# - 504: Gateway Timeout
# - 599: Network Timeout

# -------  API Requests -------
# Een stappenplan om met de requests library te werken:

# Import:
# - Importeer de requests module om een request te kunnen maken.
# URL:
# - Specificeer de URL van de request om het pad naar de gewenste resource te bepalen.
# - (optie: ook de data, headers en params toevoegen)
# API_KEY:
# - Veel API's eisen een API_KEY. Daarvoor zul je je moeten registreren.
# - Dit is meestal om spammen en overbelasting van de server te voorkomen, maar ook om betaalservices te valideren.
# Request:
# - Maak het request met de requests library.
# Type:
# - Kies de juiste HTTP-methode (GET, POST, PUT, DELETE) voor de interactie met de API.
# Status check:
# - Controleer of de response een statuscode 200 heeft, wat duidt op succes.
# Response:
# - Ontvang een response van de API, meestal in JSON of XML formaat, die de gevraagde data of de status bevat.





