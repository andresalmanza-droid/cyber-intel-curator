import json

with open("data/news_clean.json") as f:
    news = json.load(f)

text = "\n".join([n["title"] for n in news])

prompt = f"""
Actúa como curador de noticias de ciberseguridad.

Con las siguientes noticias crea un boletín.

{text}
"""

print(prompt)
