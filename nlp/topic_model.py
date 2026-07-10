from sklearn.feature_extraction.text import CountVectorizer

from sklearn.decomposition import LatentDirichletAllocation


class TopicModel:

    def fit(self, texts):

        vectorizer = CountVectorizer()

        X = vectorizer.fit_transform(texts)

        lda = LatentDirichletAllocation(

            n_components=5,

            random_state=42

        )

        lda.fit(X)

        return lda
