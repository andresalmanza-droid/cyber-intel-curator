import json
from collections import Counter

INPUT_FILE = "data/news_selected.json"
OUTPUT_FILE = "data/news_signals.json"

def classify_signal(title):

    title = title.lower()

    weak_keywords = [
        "researchers",
        "study",
        "analysis",
        "experiment",
        "new technique",
        "ai agents",
        "attack surface"
    ]

    emerging_keywords = [
        "campaign",
        "targets",
        "abused",
        "backdoor",
        "espionage",
        "apt"
    ]

    consolidated_keywords = [
        "critical vulnerability",
        "ransomware activity",
        "mass exploitation",
        "widespread"
    ]

    for k in weak_keywords:
        if k in title:
            return "weak_signal"

    for k in emerging_keywords:
        if k in title:
            return "emerging_threat"

    for k in consolidated_keywords:
        if k in title:
            return "consolidated_threat"

    return "general_signal"


def main():

    with open(INPUT_FILE) as f:
        news = json.load(f)

    signals = []

    for n in news:

        title = n.get("title","")

        signal_type = classify_signal(title)

        n["signal"] = signal_type

        signals.append(n)

    with open(OUTPUT_FILE,"w") as f:
        json.dump(signals,f,indent=2)

    print("Signal classification completed")


if __name__ == "__main__":
    main()
