from scraper.news_scraper import NewsScraper

from etl.clean import clean

from etl.transform import transform

from etl.load import load


def run_pipeline():

    scraper = NewsScraper()

    df = scraper.scrape()

    df = clean(df)

    df = transform(df)

    load(df, "news")

    print("Pipeline completed.")
