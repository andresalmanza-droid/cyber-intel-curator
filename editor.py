import json
from collections import defaultdict

with open("data/news_classified.json") as f:
    news = json.load(f)

sections = defaultdict(list)

for n in news:
    sections[n["category"]].append(n)

newsletter = ""

for sec,items in sections.items():

    newsletter += f"\n\n{sec.upper()}\n"

    for i in items[:3]:

        newsletter += f"- {i['title']} ({i['source']})\n"

print(newsletter)
