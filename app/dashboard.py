import streamlit as st

import pandas as pd

from sqlalchemy import create_engine


engine = create_engine(

    "sqlite:///data/database.db"

)


st.title("AI Job & News Analytics")


df = pd.read_sql(

    "SELECT * FROM news",

    engine

)


search = st.text_input(

    "Search"

)


if search:

    df = df[

        df["title"]

        .str.contains(

            search,

            case=False

        )

    ]


st.dataframe(df)
