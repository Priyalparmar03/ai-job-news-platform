from etl.database import engine


def load(df, table_name):

    df.to_sql(

        table_name,

        engine,

        if_exists="append",

        index=False

    )
