import requests
from bs4 import BeautifulSoup

def search_torrents(query: str):
    url = f"https://www.1337x.to/search/{query}/1/"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    results = []
    for row in soup.select("table.table-list tbody tr"):
        title = row.select_one("td.name a:nth-of-type(2)").text
        link = "https://www.1337x.to" + row.select_one("td.name a:nth-of-type(2)")["href"]
        results.append((title, link))
    
    return results

torrent = search_torrents("All Quiet on the Western Front")