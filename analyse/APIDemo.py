import requests

BASE_URL = "http://127.0.0.1:5000"
ENDPOINT = "/predict"
payload = {"data": "elonmusk"}
response = requests.post(BASE_URL + ENDPOINT, json=payload)
print(response.json())
