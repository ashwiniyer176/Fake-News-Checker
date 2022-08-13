"""
Contains all the routes that are required for the app's API's or website Functionality
Keep in mind that imports specfic to a seprate function is to be done in its own file
"""


from flask import render_template, request, Flask
from analyse import app
from analyse.externalFileExample import JokesFunction
from analyse.prediction import predictor
from .twitterbot import TwitterBot
from .JoyModel import JoyModel
from .FakeModel import FakeModel


# from analyse.pdfGeneration import createPdf


def zip_lists(list1, list2):
    return list(zip(list1, list2))


model = FakeModel("./models/FakeNewsANN.h5")


@app.route("/")
def Home():

    return render_template("HomePage.html", isHome=False)


@app.route("/input")
def inputFourm():
    return render_template("predict.html")


@app.route("/tweets", methods=["GET", "POST"])
def getTweets():
    # Finds the most recent tweets of the given user ID
    if request.method == "POST":
        form = request.form
        twitterID = form["twitterID"]
        bot = TwitterBot()
        bot.authenticate()
        tweets = bot.getTweetsByUser(twitterID)
        if tweets is not None:
            output = model.predict(tweets)
            prediction = zip_lists(tweets, output)
            return render_template(
                "results.html", user=twitterID, prediction=prediction
            )
        else:
            return render_template("tweets.html", message="Invalid User ID")
    # Returns a form to get the user ID
    else:
        return render_template("tweets.html")


@app.route("/output", methods=["POST"])
def predictReq():
    if request.method == "POST":
        lol = request.form
        answer = predictor(lol["VALUE ENTERED"])
        answer = f"The sentence shows {answer*100:.2f}% joy."
        return render_template(
            "Result page.html", value=answer, input=lol["VALUE ENTERED"]
        )


@app.route("/predict", methods=["POST"])
def predictSentiment():
    # API Endpoint for the Chrome Extension

    data = request.get_json()
    print(data["data"])
    bot = TwitterBot()
    bot.authenticate()
    tweets = bot.getTweetsByUser(data["data"])
    output = model.predict(tweets)
    print("Output: ", output)
    prediction = zip_lists(tweets, output)
    print(prediction)
    response = {"prediction": prediction}
    return response


@app.route("/DownloadReport", methods=["POST"])
def DownloadReport():
    lol = request.form
    webPage = render_template("Result page.html", value=lol["1"], input=lol["2"])
    response = createPdf(webPage)
    return response


@app.route("/funny")
def funnyJoke():
    return JokesFunction()
