from concurrent.futures import ThreadPoolExecutor
import socket

def escanear_puerto(puerto):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect(("127.0.0.1", puerto))
        s.close()
        return puerto
    except:
        return None

with ThreadPoolExecutor(max_workers=100) as executor:
    resultados = list(executor.map(escanear_puerto, range(1, 1025)))

puertos_abiertos = [r for r in resultados if r is not None]

for puerto in sorted(puertos_abiertos):
    print(f"[+] Puerto {puerto} abierto")