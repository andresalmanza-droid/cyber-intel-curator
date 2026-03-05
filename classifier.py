import json

with open("data/news_clean.json") as f:
    news = json.load(f)

categories = {
    "geopolitica":[
        "nation state","government","iran","china","russia",
        "cyber war","sanctions","espionage"
    ],

    "vulnerabilidades":[
        "vulnerability","cve","patch","exploit",
        "zero day","0day"
    ],

    "ransomware":[
        "ransomware","extortion","lockbit",
        "blackcat","decrypt"
    ],

    "brechas":[
        "data breach","leak","exposed data",
        "stolen data"
    ],

    "ciberataques":[
        "attack","malware","campaign",
        "phishing","botnet"
    ],

    "ia":[
        "ai","artificial intelligence",
        "llm","machine learning"
    ],

    "riesgo":[
        "cyber risk","resilience",
        "business continuity"
    ]
}

classified = []

for item in news:

    title = item["title"].lower()

    found = "algo_mas"

    for cat,words in categories.items():

        for w in words:

            if w in title:

                found = cat

    item["category"] = found
    classified.append(item)

with open("data/news_classified.json","w") as f:
    json.dump(classified,f,indent=2)
