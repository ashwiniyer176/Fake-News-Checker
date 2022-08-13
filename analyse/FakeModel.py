import tensorflow as tf
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
import regex as re
import string

from . import models


class FakeModel(models.NLPModel):
    """
    A class that helps use an NLP model by implementing a few major functions
    """

    def __init__(self, model_weights):
        super().__init__(model_weights)

    def load_model(self, model_weights):
        """
        Function to load the model from a serialized set of weights

        Args:
            model_weights (string): Path to the file containing serialized model weights

        Returns:
            model: A model with the required set of weights
        """
        model = tf.keras.models.load_model(model_weights)
        return model

    def preprocess(self, text, DIMS=100):
        """
        Preprocessing function for the given model
        Args:
            text (string): The text input for the model

        Returns:
            processed_text: The processed text that can directly be fed into the model
        """

        clean_text = self.cleanText(text)
        vec = self.getGloveCorpus()
        processed_text = self.getVecForm(X=clean_text, dims=DIMS, vec=vec)
        return processed_text

    def getGloveCorpus(self):
        # Set path and load corpus
        path = "./data/sources/"
        filename = "Glove.csv"
        vec = pd.read_csv(path + filename, index_col=0)
        return vec

    def getGloveVec(self, word, vec, dims=100):
        vc = np.zeros(dims)
        try:
            vc = np.array(vec.loc[word])
        except:
            vc = np.zeros(dims)
        return vc

    def getDocVec(self, sentence, dims, vec):
        tokens = word_tokenize(sentence)
        vecs = np.zeros(dims)

        for word in tokens:
            vecs += self.getGloveVec(word, vec, dims)

        return vecs

    def getVecForm(self, X, dims, vec):
        vecList = []

        for i in X:
            vecList.append(self.getDocVec(i, dims, vec))
        X = np.asarray(vecList).astype(np.float16)

        return X

    def cleanText(self, textData):
        cleanText = []

        for i in textData:
            # convert to lowercase
            new = i.lower()

            # remove urls
            url = re.compile(r"https?://\S+|www\.\S+")
            new = url.sub(r"", new)

            # remove html tags
            html = re.compile(r"<.*?>")
            new = html.sub(r"", new)

            # remove punctuation
            operator = str.maketrans("", "", string.punctuation)
            new = new.translate(operator)
            cleanText.append(new)
        return cleanText

    def predict(self, tweets):
        predictions = []
        for tweet in tweets:
            processed_text = self.preprocess(tweet)
            predictions.append(self.model.predict(processed_text)[0][0] * 100)
        return predictions
