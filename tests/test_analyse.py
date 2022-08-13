import os
import tempfile
from analyse import models, twitterbot
import pytest
import analyse


@pytest.fixture
def client():
    db_fd, analyse.app.config["DATABASE"] = tempfile.mkstemp()
    analyse.app.config["TESTING"] = True

    with analyse.app.test_client() as client:
        with analyse.app.app_context():
            analyse.init_db()
        yield client

    os.close(db_fd)
    os.unlink(analyse.app.config["DATABASE"])


class Sample(models.NLPModel):
    def __init__(self, model_weights):
        super().__init__(model_weights)

    def load_model(self, model_weights):
        return super().load_model(model_weights)

    def preprocess(self, text):
        return super().preprocess(text)

    def predict(self, text):
        return super().predict(text)


def test_NLPModel_raises_NotImplementedError():
    with pytest.raises(NotImplementedError):
        model = models.NLPModel("./models/Best_Joy.sav")


def test_Sample_raises_NotImplementedError():
    with pytest.raises(NotImplementedError):
        model = Sample("./models/Best_Joy.sav")


def test_after_authenticate():
    bot = twitterbot.TwitterBot()
    assert bot.isAuthenticated() == False
    bot.authenticate()
    assert bot.isAuthenticated() == True


def test_valid_userID():
    bot = twitterbot.TwitterBot()
    bot.authenticate()
    assert bot.isUserIDValid("unclebobmartin") == True


def test_invalid_userID():
    bot = twitterbot.TwitterBot()
    bot.authenticate()
    assert bot.isUserIDValid("unclebobmarti") == False


def test_tweets_are_not_empty():
    bot = twitterbot.TwitterBot()
    bot.authenticate()
    tweets = bot.getTweetsByUser("unclebobmartin")
    assert len(tweets) > 0
