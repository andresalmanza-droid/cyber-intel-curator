import json
import re
from collections import Counter
from pathlib import Path

STOPWORDS = {
    "the","a","an","to","of","in","on","for","and","with",
    "new","report","shows","reveals","after","more"
}

DATA_PATH = Path("data/news_selected.json")
OUTPUT_PATH = Path("data/keyword_trends.json")


def extract_keywords(entries):

    words = []

    for entry in entries:

        title = entry.get("title","").lower()

        tokens = re.findall(r"\b[a-z]{3,}\b", title)

        for t in tokens:
            if t not in STOPWORDS:
                words.append(t)

    counter = Counter(words)

    return counter.most_common(10)


if __name__ == "__main__":

    with open(DATA_PATH) as f:
        entries = json.load(f)

    keywords = extract_keywords(entries)

    result = []

    for word, count in keywords:
        result.append({
            "keyword": word,
            "mentions": count
        })

    with open(OUTPUT_PATH, "w") as f:
        json.dump(result, f, indent=2)

    print("Keyword trends saved to", OUTPUT_PATH)
