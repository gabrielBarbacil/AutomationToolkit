import socket
import threading

resultados = []
lock = threading.Lock()

def escanear_puerto(ip, puerto):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, puerto))
        s.close()
        with lock:
            resultados.append(puerto)
    
    except:
        pass

ip = "127.0.0.1"
hilos = []

for puerto in range(1, 1025):
    t = threading.Thread(target=escanear_puerto, args=(ip, puerto))
    hilos.append(t)
    t.start()

for t in hilos:
    t.join()

for puerto in sorted(resultados):
    print(f"[+] Puerto {puerto} abierto")