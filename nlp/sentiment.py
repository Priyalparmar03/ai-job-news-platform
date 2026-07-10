from transformers import pipeline


classifier = pipeline(

    "sentiment-analysis"

)


def analyze(text):

    return classifier(text)[0]
