import requests

def brute_http(args):
    url, usuario, password = args
    r = requests.post(url, data={"username": usuario, "password": password})
    if r.status_code == 200:
        return {"url": url, "usuario": usuario, "password": password}
    else:
        return None

