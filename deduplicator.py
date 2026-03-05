import json
from difflib import SequenceMatcher

with open("data/news_raw.json") as f:
    news = json.load(f)

unique = []

for item in news:

    duplicate = False

    for u in unique:

        ratio = SequenceMatcher(None,item["title"],u["title"]).ratio()

        if ratio > 0.8:
            duplicate = True

    if not duplicate:
        unique.append(item)

with open("data/news_clean.json","w") as f:
    json.dump(unique,f,indent=2)
