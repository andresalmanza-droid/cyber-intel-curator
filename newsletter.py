import json
from datetime import date
import os

# cargar noticias seleccionadas
with open("data/news_selected.json") as f:
    news = json.load(f)

today = date.today()

# construir el boletín
newsletter = ""
newsletter += "# Cyber Intelligence Brief\n"
newsletter += f"Date: {today}\n\n"
newsletter += "Curated cybersecurity signals of the week.\n\n"

for n in news:

    title = n.get("title", "No title")
    summary = n.get("summary", "")
    url = n.get("url", "No source available")
    category = n.get("category", "general")

    newsletter += f"## {title}\n"

    if summary:
        newsletter += f"{summary}\n\n"

    newsletter += f"Source: {url}\n"
    newsletter += f"Category: {category}\n\n"

# asegurar que la carpeta newsletter exista
os.makedirs("newsletter", exist_ok=True)

# guardar boletín
filename = f"newsletter/cyberintel-{today}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(newsletter)

print("Newsletter created:", filename)
