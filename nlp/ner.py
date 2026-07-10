from transformers import pipeline


ner = pipeline(

    "ner",

    aggregation_strategy="simple"

)


def extract_entities(text):

    return ner(text)
