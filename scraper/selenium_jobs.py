from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time


class SeleniumJobScraper:

    def __init__(self, headless=True):

        options = Options()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options=options)

    def scrape(self, url):

        self.driver.get(url)

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "body")
            )
        )

        time.sleep(3)

        jobs = []

        cards = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div.job-card"
        )

        for card in cards:

            try:

                title = card.find_element(
                    By.CSS_SELECTOR,
                    ".job-title"
                ).text

            except:
                title = ""

            try:

                company = card.find_element(
                    By.CSS_SELECTOR,
                    ".company"
                ).text

            except:
                company = ""

            try:

                location = card.find_element(
                    By.CSS_SELECTOR,
                    ".location"
                ).text

            except:
                location = ""

            try:

                link = card.find_element(
                    By.TAG_NAME,
                    "a"
                ).get_attribute("href")

            except:
                link = ""

            jobs.append({

                "title": title,
                "company": company,
                "location": location,
                "url": link

            })

        return pd.DataFrame(jobs)

    def close(self):

        self.driver.quit()


if __name__ == "__main__":

    scraper = SeleniumJobScraper()

    df = scraper.scrape("https://example-job-site.com")

    print(df.head())

    scraper.close()
