#funcion escanear_puerto
#solo recibe (ip, puerto)
#devuelve un diccionario o None

import socket

def escaneo_puerto(args):
    ip, puerto = args
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, puerto))
        s.close()
        return {"puerto": puerto, "estado": "abierto"}
    except:
        return None
