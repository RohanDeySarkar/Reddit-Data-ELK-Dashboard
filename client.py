import requests
import json
import time

# Server URL
url = 'http://127.0.0.1:8080'

f = open('redditData.json')

json_data = json.load(f)

print(json_data)

count = 0
for i in json_data:
    requests.post(url, json = i)
    count += 1
    print(count)

print("Sent to server successfully!!")