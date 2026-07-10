import pandas as pd

from scraper.base_scraper import BaseScraper


class NewsScraper(BaseScraper):

    def scrape(self):

        url = "https://news.ycombinator.com/"

        soup = self.get_page(url)

        records = []

        for title in soup.select(".titleline a"):

            records.append({

                "title": title.text,

                "url": title.get("href")

            })

        return pd.DataFrame(records)
