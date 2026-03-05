import json
import re

with open("data/news_raw.json") as f:
    news = json.load(f)

clean_news = []

for n in news:

    title = n.get("title","").strip()
    summary = n.get("summary","").strip()

    # eliminar títulos muy cortos
    if len(title) < 10:
        continue

    # eliminar publicidad o CTA
    blacklist = [
        "subscribe",
        "advertisement",
        "reach out",
        "contact us",
        "submit news",
        "sponsored",
        "demo",
        "register"
    ]

    if any(word in title.lower() for word in blacklist):
        continue

    # eliminar CVE sueltos
    if re.match(r"CVE-\d{4}-\d+", title):
        continue

    clean_news.append({
        "title": title,
        "summary": summary,
        "source": n.get("source")
    })

with open("data/news_clean.json","w") as f:
    json.dump(clean_news,f,indent=2)

print("Cleaning completed")
