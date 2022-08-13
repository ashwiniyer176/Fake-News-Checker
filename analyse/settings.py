from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
API_KEY = os.environ["API_KEY"]
API_KEY_SECRET = os.environ["API_KEY_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]
SESSION_COOKIE_SECURE = True
