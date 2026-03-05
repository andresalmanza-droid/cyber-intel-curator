import json
from collections import defaultdict

with open("data/news_classified.json") as f:
    news = json.load(f)

sections = defaultdict(list)

for n in news:
    category = n.get("category","Otros")
    sections[category].append(n)

selected = []

for category, items in sections.items():

    # tomar máximo 3
    top = items[:3]

    for n in top:
        selected.append(n)

with open("data/news_selected.json","w") as f:
    json.dump(selected,f,indent=2)

print("Selection completed")
