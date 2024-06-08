
#PRIMERO IR A SPOTIFY DEVELOPERS


#API. Base de dades per exemple relacional amb diferents dades.
#El meu ordinador consulta una API. LA API demana permisos. Depenent de tot això es fa la consulta. La consulta torna a la API.
#Finalment la api ens dona un arxiu jason amb tota la informació.

#EL que no es troba a developers de la app no es pot fer. con spotipy tenemos una librería que nos facilita la extracción de datos de Spotify con la API.
#DASHBOARD CREAR APP PARA EL TOKEN OBTENERLO


import json

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


api_client_id = ""
api_client_secret = ""   #es un token que solo sabemos nosotros y spotify

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))
artista_inicial = "7ltDVBr6mKbRvohxheJ9h1"
resposta = spotify.artist_related_artists(artista_inicial)


with open('data_2.json', 'w', encoding='utf-8') as f:
   json.dump(resposta, f, indent=4)

llista_artistes = []

artistes = resposta["artists"]
for a in artistes:
    name = a["name"]
    seguidores = a["followers"]["total"]
    link = a["external_urls"]["spotify"]
    id = a["id"]


    frame = pd.DataFrame({   #
        "semilla": id,
        "name": name,
        "id": id,
        "seguidors": seguidores,
        "link": link,

    },index=[0])

    llista_artistes.append(frame)

    resposta2 = spotify.artist_related_artists(id)
    artistes2 = resposta2["artists"]
    for a in artistes:
        name = a["name"]
        seguidores = a["followers"]["total"]
        link = a["external_urls"]["spotify"]
        id = a["id"]

        frame = pd.DataFrame({  #
            "semilla": id,
            "name": name,
            "id": id,
            "seguidors": seguidores,
            "link": link,

        }, index=[0])

        llista_artistes.append(frame)


final = pd.concat(llista_artistes)
print(final)
final.to_excel("dataset_2.xlsx")
