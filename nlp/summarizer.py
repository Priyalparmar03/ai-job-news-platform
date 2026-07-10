from transformers import pipeline


summarizer = pipeline(

    "summarization"

)


def summarize(text):

    return summarizer(

        text,

        max_length=80,

        min_length=20

    )[0]["summary_text"]
