from transformers import pipeline


class TextClassifier:

    def __init__(self):

        self.zero_shot = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )

        self.labels = [

            "Artificial Intelligence",
            "Machine Learning",
            "Data Science",
            "Software Engineering",
            "Cyber Security",
            "Cloud Computing",
            "Business",
            "Finance",
            "Healthcare",
            "Education"

        ]

    def classify(self, text):

        result = self.zero_shot(

            text,

            candidate_labels=self.labels

        )

        return {

            "label": result["labels"][0],

            "score": round(result["scores"][0], 3)

        }


if __name__ == "__main__":

    model = TextClassifier()

    text = """
    OpenAI releases new GPT model for enterprise AI.
    """

    print(model.classify(text))
