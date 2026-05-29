import argparse
from scanner import escaneo_puerto
from fuzzer import fuzz_directorio
import json
from concurrent.futures import ThreadPoolExecutor
from brute import brute_http
from spider import spider



parser = argparse.ArgumentParser(description="Automation Toolkit")
subparsers = parser.add_subparsers(dest="comando")


# scan subcomando
scan_parser = subparsers.add_parser("scan", help="escaneo puertos")
scan_parser.add_argument("-t", "--target", required=True)
scan_parser.add_argument("-p", "--puertos", default="1-1024")

# dir subcomando
fuzz_parser = subparsers.add_parser("fuzz", help="fuzz de directorios")
fuzz_parser.add_argument("-u", "--url", required=True)
fuzz_parser.add_argument("-w", "--wordlist", required=True)

# brute subcomando
brute_parser = subparsers.add_parser("brute", help="modo bruteforce")
brute_parser.add_argument("-u", "--url", required=True)
brute_parser.add_argument("-U", "--usernames", required=True)
brute_parser.add_argument("-w", "--wordlist", required=True)

# spider subcomando
spider_parser = subparsers.add_parser("spider", help="web scrapping")
spider_parser.add_argument("-u", "--url", required=True)


args = parser.parse_args()
WORKERS = 100


if args.comando == "scan":
    inicio, fin = args.puertos.split("-")
    rango = range(int(inicio), int(fin) + 1)
    tareas = [(args.target, puerto) for puerto in rango]
    #resultado = escaneo_puerto(("127.0.0.1", 135))
    #print(resultado)
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        resultados = list(executor.map(escaneo_puerto, tareas))

    abiertos = [r for r in resultados if r is not None]

    output = {
        "target": args.target,
        "puertos_escaneados": f"{args.puertos}",
        "puertos_abiertos": abiertos
    }

    with open("scan_puertos.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

    print(f"\n[*] Resultados guardados en scan_puertos.json")


elif args.comando == "fuzz":
    with open(args.wordlist, "r") as f:
        palabras = [linea.strip() for linea in f]
    tareas = [(args.url, palabra) for palabra in palabras]
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        directorios = list(executor.map(fuzz_directorio, tareas))

    output = {
        "url": args.url,
            "directorios_encontrados": [d for d in directorios if d is not None]
    }

    with open("fuzz_dirs.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

    print(f"\n[*] Resultados guardados en fuzz_dirs.json")

elif args.comando == "brute":
    with open(args.wordlist, "r") as b:
        passwords = [linea.strip() for linea in b]
    with open(args.usernames, "r") as c:
        usuarios = [linea.strip() for linea in c]
    tareas = [(args.url, usuario, password) for usuario in usuarios for password in passwords] 
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        credenciales = list(executor.map(brute_http, tareas))

    output = {
        "url": args.url,
            "credenciales_encontrados": [e for e in credenciales if e is not None]
    }

    with open("creds.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

    print(f"\n[*] Resultados guardados en creds.json")

elif args.comando == "spider":
    resultados = spider(args.url)
    
    output = {
    "url": args.url,
    "paginas_encontradas": resultados
    }

    with open("resultados.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)