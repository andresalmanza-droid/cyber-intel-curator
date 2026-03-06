import json
from datetime import datetime
from collections import defaultdict

with open("data/news_intel.json") as f:
    news = json.load(f)

signals = defaultdict(list)

for n in news:
    signals[n["signal"]].append(n)

today = datetime.utcnow().strftime("%Y-%m-%d")

brief = f"""Cyber Intelligence Brief
Date: {today}

Strategic cybersecurity signals identified this week.

"""

for signal_type, items in signals.items():

    brief += f"\n=== {signal_type.upper()} ===\n\n"

    for n in items:

        title = n.get("title","")
        url = n.get("url","")

        brief += f"{title}\n"
        brief += f"Source: {url}\n\n"

with open("newsletter/cyber_intel_brief.txt","w") as f:
    f.write(brief)

print("Cyber intelligence brief generated")
