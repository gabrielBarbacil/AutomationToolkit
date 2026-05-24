import argparse
import json
import socket
from concurrent.futures import ThreadPoolExecutor

resultados = []

def escanear_puerto(args):
    ip, puerto = args
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, puerto))
        try:
            s.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = s.recv(1024).decode(errors="ignore").strip()
        except:
            banner = ""
        s.close()
        return {"puerto": puerto, "banner": banner}
    except:
        return None

parser = argparse.ArgumentParser(description="Port scanner")
parser.add_argument("-t", "--target", required=True, help="IP objetivo")
parser.add_argument("-p", "--puertos", default="1-1024", help="Rango de puertos (ej: 1-1024)")
parser.add_argument("-w", "--workers", type=int, default=100, help="Hilos simultáneos")
args = parser.parse_args()

inicio, fin = args.puertos.split("-")
rango = range(int(inicio), int(fin) + 1)
tareas = [(args.target, puerto) for puerto in rango]

print(f"\n[*] Escaneando {args.target} puertos {args.puertos} con {args.workers} hilos...\n")

with ThreadPoolExecutor(max_workers=args.workers) as executor:
    resultados = list(executor.map(escanear_puerto, tareas))

abiertos = [r for r in resultados if r is not None]

for r in sorted(abiertos, key=lambda x: x["puerto"]):
    print(f"[+] Puerto {r['puerto']} abierto")
    if r["banner"]:
        for linea in r["banner"].split("\r\n"):
            if any(k in linea for k in ["Server:", "SSH", "220", "HTTP"]):
                print(f"    └─ {linea}")



output = {
    "target": args.target,
    "puertos_escaneados": f"{args.puertos}",
    "puertos_abiertos": abiertos
}

with open("resultados.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4)

print(f"\n[*] Resultados guardados en resultados.json")