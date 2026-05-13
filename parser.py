import requests
from bs4 import BeautifulSoup

def search_companies(query):
    url = f"https://www.bing.com/search?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    results = []

    for item in soup.select("li.b_algo"):
        title_tag = item.select_one("h2")
        snippet_tag = item.select_one(".b_caption p")

        title = title_tag.text.strip() if title_tag else ""
        snippet = snippet_tag.text.strip() if snippet_tag else ""

        if title:
            results.append({
                "company": title,
                "info": snippet
            })

    return results[:20]
