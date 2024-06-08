
El siguiente código realiza varias tareas relacionadas con la extracción y procesamiento de datos de Eurovisión y Spotify.

1. Extracción de Datos de Wikipedia
Mediante librerías requests y BeautifulSoup para la extracción de datos de las páginas de Wikipedia sobre el Festival Eurovisión.
Se procesa el HTML de las páginas web, encuentra la tabla de resultados finales y la información es almacenada en archivos Excel haciendo uso de pandas.

2. Unión de Datos
Une los archivos Excel generados en un único DataFrame y almacena el resultado en un archivo Excel final.
Utiliza la librería glob para encontrar y procesar varios archivos Excel.

3. Búsqueda en Spotify
Con spotipy se hace una búsqueda de cada canción y artista en Spotify.
Los resultadon se guardan en un archivo JSON.

Se utilizan las siguiente herramientas:
Python
Librerías Python: requests, BeautifulSoup, pandas, glob y spotipy.
Wikipedia
Spotify: Fuente de datos para información sobre canciones y artistas.
