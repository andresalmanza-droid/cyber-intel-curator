from datetime import datetime

HEADER_TITLE = "Cyber Intelligence Brief"
HEADER_DESCRIPTION = "Curated cybersecurity signals of the week."


def clean_title(title: str) -> str:
    """
    Cleans titles from ads, extra whitespace, or newsletter artifacts.
    """
    if not title:
        return ""

    # remove excessive whitespace
    title = " ".join(title.split())

    # remove promotional phrases
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
    """
    Ensures the entry has the minimum fields required.
    """
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
    """
    Formats one entry for the newsletter.
    """
    title = clean_title(entry["title"])

    if not title:
        return ""

    url = entry["url"]
    category = entry["category"]

    return f"""{title}
Source: {url} Category: {category}
"""


def build_newsletter(entries: list) -> str:
    """
    Builds the full newsletter text.
    """
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

    # Example structure expected from your pipeline
    example_entries = [
        {
            "title": "Weekly Recap: SD-WAN 0-Day, Critical CVEs, Telegram Probe, Smart TV Proxy SDK and More",
            "url": "https://thehackernews.com/2026/03/weekly-recap-sd-wan-0-day-critical-cves.html",
            "category": "vulnerabilidades"
        },
        {
            "title": "Researchers Show Copilot and Grok Can Be Abused as Malware C2 Proxies",
            "url": "https://thehackernews.com/2026/02/researchers-show-copilot-and-grok-can.html",
            "category": "ciberataques"
        }
    ]

    newsletter_text = build_newsletter(example_entries)

    print(newsletter_text)
