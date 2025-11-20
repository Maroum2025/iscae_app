import requests

req = requests.get("http://127.0.0.1:8000/say_hello/")
print(req.json()['Say Hello'])