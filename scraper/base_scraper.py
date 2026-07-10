import requests
from bs4 import BeautifulSoup


class BaseScraper:

    def get_page(self, url):

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        return BeautifulSoup(
            response.text,
            "html.parser"
        )
