import socket

def escanear_puerto(ip, puerto):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, puerto))
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = s.recv(1024).decode(errors="ignore").strip()
        s.close()
        return True, banner
    except:
        return False, ""
    
ip = "127.0.0.1"
puertos = [135, 445, 7568, 20000, 24830, 58007]

print (f"Escaneando {ip}...\n")
for puerto in puertos:
    abierto, banner = escanear_puerto(ip, puerto)
    if abierto:
        print(f"[+] {puerto} abierto")
        for linea in banner.split("\r\n"):
            if "Server:" in linea or "SSH" in linea:
                print(f"    └─ {linea}")
    else:
        print(f"[-] {puerto} cerrado")