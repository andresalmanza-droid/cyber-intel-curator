import json
from collections import Counter
import os


INPUT_FILE = "data/news_intel.json"
OUTPUT_FILE = "data/trends.json"


def load_news():
    with open(INPUT_FILE, encoding="utf-8") as f:
        return json.load(f)

IGNORED_CATEGORIES = ["algo_mas"]

def detect_category_trends(entries):

    categories = [
        e.get("category") 
        for e in entries 
        if e.get("category") and e.get("category") not in IGNORED_CATEGORIES
    ]
    counter = Counter(categories)

    trends = []

    for cat, count in counter.items():

        if count >= 3:
            trends.append({
                "type": "category_trend",
                "category": cat,
                "mentions": count
            })

    return trends


def detect_signal_trends(entries):

    signals = [e.get("signal") for e in entries if e.get("signal")]
    counter = Counter(signals)

    trends = []

    for sig, count in counter.items():

        if count >= 2:
            trends.append({
                "type": "signal_trend",
                "signal": sig,
                "mentions": count
            })

    return trends


def build_trends(entries):

    trends = []

    trends.extend(detect_category_trends(entries))
    trends.extend(detect_signal_trends(entries))

    return trends


if __name__ == "__main__":

    os.makedirs("data", exist_ok=True)

    news = load_news()

    trends = build_trends(news)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(trends, f, indent=2)

    print("Trends detected:", len(trends))
