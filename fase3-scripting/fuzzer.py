import requests
import argparse

parser = argparse.ArgumentParser(description="Fuzzer de directorios")
parser.add_argument("-u", "--url", required=True, help="URL base (ej: http://127.0.0.1:8080)")
parser.add_argument("-w", "--wordlist", required=True, help="Ruta a la wordlist")
args = parser.parse_args()

encontrados = []

with open(args.wordlist, "r") as f:
    palabras = [linea.strip() for linea in f]

print(f"\n[*] Fuzzing {args.url} con {len(palabras)} palabras...\n")

for palabra in palabras:
    url = f"{args.url}/{palabra}"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 404:
            encontrados.append(f"{r.status_code} -> {url}")
            print(f"[+] {r.status_code} -> {url}")
    except requests.exceptions.ConnectionError:
        print(f"[!] Sin conexion -> {url}")
        break
    except requests.exceptions.Timeout:
        print(f"[!] Timeout -> {url}")

with open("fuzzer_log.txt", "a", encoding="utf-8") as log:
    log.write(f"\n[*] Fuzzing {args.url}\n")
    for r in encontrados:
        log.write(f"[+] {r}\n")
              
