import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1", {"views": 99, "likes": 100})
print(response.json())
