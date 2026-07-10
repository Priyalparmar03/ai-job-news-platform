import requests
import pandas as pd


class APIScraper:

    def fetch(self):

        url = "https://jsonplaceholder.typicode.com/posts"

        data = requests.get(url).json()

        return pd.DataFrame(data)
