import tweepy
from . import settings


"""
TODO: THings to change, test and debug in TwitterBot

1. Null tweet
2. User exists but has no tweet
3. User suspended
4. User not authorized
5. Index out of range error
"""


class TwitterBot:
    """
    A simple class that abstracts away boilerplate code for accessing twitter API and makes life easier
    """

    def __init__(self):
        """
        Create a .env file in the root directory and fill in these values in the same
        """
        self.consumerKey = settings.API_KEY
        self.consumerSecret = settings.API_KEY_SECRET
        self.accessToken = settings.ACCESS_TOKEN
        self.accessTokenSecret = settings.ACCESS_TOKEN_SECRET
        self.__authenticated = False

    def authenticate(self):
        """
        Authenticates the instance
        """
        auth = tweepy.OAuth1UserHandler(self.consumerKey, self.consumerSecret)
        auth.set_access_token(self.accessToken, self.accessTokenSecret)
        api = tweepy.API(auth)
        self.__authenticated = True
        return api

    def isUserIDValid(self, userID):
        """
        Checks whether a user of given userID exists

        Args:
            userID (string): Twitter user ID

        Returns:
            status(boolean): Validity status of the user
        """
        api = self.authenticate()
        try:
            user = api.get_user(screen_name=userID)
            print("Found user")
            return True
        except tweepy.TweepyException as e:
            print(e.with_traceback())
            return False

    def getTweetsByUser(self, userID):
        """
        Gets all the tweets in the timeline of a user by their user ID

        Args:
            userID (string): A string which is the Twitter user ID

        Returns:
            tweets (list): A list of strings containing the tweets of the given user
        """
        api = self.authenticate()
        if self.isUserIDValid(userID):
            tweets = api.user_timeline(
                screen_name=userID, count=10, include_rts=False, tweet_mode="extended"
            )
            tweet_text = [tweets[i].full_text for i in range(len(tweets))]
            return tweet_text
        else:
            return None
