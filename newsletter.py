import json
from datetime import date
import os

# cargar noticias seleccionadas
with open("data/news_selected.json") as f:
    news = json.load(f)

today = date.today()

# asegurar carpeta newsletter
os.makedirs("newsletter", exist_ok=True)

# limpiar noticias inválidas
clean_news = []

for n in news:
    title = n.get("title")
    url = n.get("url")

    # solo aceptar noticias válidas
    if title and url and url.startswith("http"):
        clean_news.append(n)

# construir boletín
newsletter = f"# Cyber Intelligence Brief\n"
newsletter += f"Date: {today}\n\n"
newsletter += "Curated cybersecurity signals of the week.\n\n"

for n in clean_news:

    title = n.get("title", "No title")
    summary = n.get("summary", "")
    url = n.get("url", "No source")

    newsletter += f"## {title}\n"

    if summary:
        newsletter += f"{summary}\n\n"

    newsletter += f"Source: {url}\n\n"

# guardar boletín
filename = f"newsletter/cyberintel-{today}.md"

with open(filename, "w") as f:
    f.write(newsletter)

print("Newsletter created:", filename)
