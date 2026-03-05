import requests
from bs4 import BeautifulSoup
import yaml
import json

with open("sources.yaml") as f:
    config = yaml.safe_load(f)

news = []

for s in config["sources"]:

    source = s["name"]
    url_source = s["url"]

    r = requests.get(url_source)
    soup = BeautifulSoup(r.text, "html.parser")

    for link in soup.find_all("a"):

        title = link.get_text().strip()
        href = link.get("href")

        # evitar enlaces vacíos
        if not href:
            continue

        # evitar enlaces internos
        if not href.startswith("http"):
            continue

        # evitar textos muy cortos
        if title and len(title) > 40:

            news.append({
                "title": title,
                "url": href,
                "source": source
            })

with open("data/news_raw.json", "w") as f:
    json.dump(news, f, indent=2)

print(f"Collected {len(news)} news items")
