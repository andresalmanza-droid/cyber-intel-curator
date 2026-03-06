import json
import os
from datetime import datetime

HEADER_TITLE = "Cyber Intelligence Brief"
HEADER_DESCRIPTION = "Curated cybersecurity signals of the week."


def clean_title(title: str) -> str:
    if not title:
        return ""

    title = " ".join(title.split())

    blacklist = [
        "request demo",
        "demo",
        "sponsored",
        "advertisement",
        "airia is the governance",
    ]

    lowered = title.lower()
    for word in blacklist:
        if word in lowered:
            return ""

    return title.strip()


def is_valid_entry(entry: dict) -> bool:

    if not isinstance(entry, dict):
        return False

    if not entry.get("title"):
        return False

    if not entry.get("url"):
        return False

    if not entry.get("category"):
        return False

    return True


def format_entry(entry: dict) -> str:

    title = clean_title(entry["title"])
    signal = entry.get("signal", "")

    if not title:
        return ""

    url = entry["url"]
    category = entry["category"]

    return f"""{title}
Source: {url} Category: {category} Signal: {signal}
"""


def build_newsletter(entries: list) -> str:

    today = datetime.utcnow().strftime("%Y-%m-%d")

    newsletter = f"""{HEADER_TITLE}
Date: {today}

{HEADER_DESCRIPTION}

"""

    for entry in entries:

        if not is_valid_entry(entry):
            continue

        formatted = format_entry(entry)

        if formatted:
            newsletter += formatted + "\n"

    return newsletter.strip()


if __name__ == "__main__":

    # cargar noticias del pipeline
    with open("data/news_intel.json") as f:
        entries = json.load(f)

    newsletter_text = build_newsletter(entries)

    # asegurar carpeta newsletter
    os.makedirs("newsletter", exist_ok=True)

    today = datetime.utcnow().strftime("%Y-%m-%d")
    filename = f"newsletter/cyberintel-{today}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(newsletter_text)

    print("Newsletter created:", filename)
