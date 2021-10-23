import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "tim", "view": 100000},
        {"likes": 10000, "name": "tim", "view": 800000},
        {"likes": 35, "name": "tim", "view": 2000}]

response = requests.put(BASE + "video/3", {"likes": 10, "name": "tim", "view": 100000})
print(response.json())
input()
response = requests.get(BASE + "video/1")
print(response.json())