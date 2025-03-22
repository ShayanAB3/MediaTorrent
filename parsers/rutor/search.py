from bs4 import BeautifulSoup
from parsers.http_parser import HttpParser

class RutorSearch(HttpParser):
    url:str
    headers:dict
    results = []

    def __init__(self,search:str, * ,headers: dict = {"User-Agent": "Mozilla/5.0"}):
        self.url = f"https://rutor.info/search/{search}"
        self.headers = headers

    def parse(self,soup: BeautifulSoup):
        torrents = soup.find_all("tr",class_=["gai", "tum"])
        space_nbsp = ("\xa0"," ")

        for torrent in torrents:
            td_all = torrent.find_all("td",align="right")
            td_text:str = td_all[0].text if len(td_all) == 1 else td_all[1].text

            self.results.append({
                "title": torrent.select("a")[2].text,
                "size": td_text.replace(*space_nbsp),
                "date": torrent.select("td")[0].text.replace(*space_nbsp),
                "link_magnet": torrent.select("a")[1]["href"],
                "link_download": "https:" + torrent.select("a")[0]["href"]
            })