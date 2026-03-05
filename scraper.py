import requests
from bs4 import BeautifulSoup
import yaml
import json

with open("sources.yaml") as f:
    config = yaml.safe_load(f)

news = []

for s in config["sources"]:

    r = requests.get(s["url"])
    soup = BeautifulSoup(r.text,"html.parser")

    for link in soup.find_all("a"):

        title = link.get_text().strip()
        href = link.get("href")

        if title and len(title) > 40:

            if not url.startswith("http"):
                 continue
                    
            news.append({
            "title": title,
            "url": url,
            "source": source
           })

with open("data/news_raw.json","w") as f:
    json.dump(news,f,indent=2)
