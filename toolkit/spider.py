import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def spider(url_base):
    visitados = set()
    #visitados.add(url_base)
    por_visitar = [url_base]
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
                    if url_base in url_completa and url_completa not in visitados:
                        por_visitar.append(url_completa)
        
        except Exception:
            pass

    return list(visitados)


