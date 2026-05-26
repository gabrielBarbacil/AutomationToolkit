import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse

parser = argparse.ArgumentParser(description="Web Spider")
parser.add_argument("-u", "--url", required=True, help="URL base")
args = parser.parse_args()

visitados = set()
por_visitar = [args.url]

print(f"\n[*] Iniciando spider en {args.url}\n")

while por_visitar:
    url_actual = por_visitar.pop(0)

    if url_actual in visitados:
        continue

    try:
        r = requests.get(url_actual, timeout=5)
        visitados.add(url_actual)
        print(f"[*] {r.status_code} -> {url_actual}")

        soup = BeautifulSoup(r.text, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href:
                url_completa = urljoin(url_actual, href)
                if args.url in url_completa and url_completa not in visitados:
                    por_visitar.append(url_completa)

    except Exception:
        pass

print(f"\n[*] Total paginas visitadas: {len(visitados)}")