# escribe una función fuzzear_directorio(url, palabra) 
# que haga una petición GET 
# devuelva un diccionario si el status no es 404, o None si lo es.

import requests

def fuzz_directorio(args):
    url, palabra = args
    url_completa = f"{url}/{palabra}"
    r = requests.get(url_completa, timeout=5)
    if r.status_code != 404:
        return{"url": url_completa, "status": r.status_code }
    else:
        return None
