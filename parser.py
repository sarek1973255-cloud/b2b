import requests
from bs4 import BeautifulSoup

def search_companies(query):
    results = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = f"https://www.google.com/search?q={query}"

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    for g in soup.find_all("div"):
        text = g.get_text(" ", strip=True)

        if "+" in text or "@" in text:
            results.append({
                "company": text[:80],
                "phone": extract_phone(text),
                "email": extract_email(text)
            })

    return results[:20]


def extract_phone(text):
    words = text.split()

    for w in words:
        if "+" in w and len(w) > 8:
            return w

    return ""


def extract_email(text):
    words = text.split()

    for w in words:
        if "@" in w:
            return w

    return ""
