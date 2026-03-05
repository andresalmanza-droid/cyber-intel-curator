import json
from datetime import date

# cargar noticias limpias
with open("data/news_clean.json") as f:
    news = json.load(f)

today = date.today()

# construir el boletín
newsletter = f"# Cyber Intelligence Brief\n"
newsletter += f"Date: {today}\n\n"
newsletter += "Curated cybersecurity signals of the week.\n\n"

for n in news:
    newsletter += f"## {n['title']}\n"
    newsletter += f"{n['summary']}\n\n"
    newsletter += f"Source: {n['url']}\n\n"

# guardar boletín
filename = f"newsletter/cyberintel-{today}.md"

with open(filename, "w") as f:
    f.write(newsletter)

print("Newsletter created:", filename)
