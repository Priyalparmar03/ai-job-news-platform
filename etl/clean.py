import pandas as pd


def clean(df):

    df = df.drop_duplicates()

    df = df.fillna("Unknown")

    return df
