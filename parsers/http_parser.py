import requests

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

class HttpParser(ABC):
    url:str
    headers:dict

    @abstractmethod
    def parse(self, soup:BeautifulSoup):
        pass

    def start(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")
        self.parse(soup)