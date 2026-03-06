import json

with open("data/news_signals.json") as f:
    news = json.load(f)

filtered = []

blacklist = [
    "request demo",
    "advertisement",
    "sponsored",
    "register now",
    "webinar"
]

for n in news:

    title = n.get("title","").lower()

    # eliminar publicidad
    if any(b in title for b in blacklist):
        continue

    # eliminar listados de CVE puros
    if title.startswith("cve-"):
        continue

    filtered.append(n)

with open("data/news_intel.json","w") as f:
    json.dump(filtered,f,indent=2)

print("Signal filtering completed")
