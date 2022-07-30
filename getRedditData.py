import requests
import json

class RedditData:
  def __init__(self, id, secret, username, password):
    auth = requests.auth.HTTPBasicAuth(id, secret)
    data = {'grant_type': 'password', 'username': username, 'password': password}
    headers = {'User-Agent': 'MyBot/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    self.headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    # requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

  def fetchData(self, base_url, subReddits):
    elasticData = []

    for subReddit in subReddits:
      res = requests.get(base_url + subReddit + "/hot", headers=self.headers, params={"limit":"100"})
      data = res.json()["data"]["children"]
      # print(data)
      for element in data:
        elementData = element["data"]
        # print(elementData)
        title = elementData["title"]
        upvotes = elementData["ups"]
        downvotes = elementData["downs"]
        commentCount = elementData["num_comments"]
        author = elementData["author"]

        tempDic = {
            "subReddit": subReddit,
            "Title": title,
            "Up Votes": upvotes,
            "Down Votes": downvotes,
            "Author": author,
            "Comment Count": commentCount
        }

        # print(tempDic)

        elasticData.append(tempDic)
      
    return elasticData

CLIENT_ID = 'oNaSFwSgYv1riYbi-KkPOg'
CLIENT_SECRET = 'zQn0DqqDrs98uDDIZO1hE4ZrtB_qiw'
USERNAME = 'wrohan'
PASSWORD = 'nokianokia000'

redditData = RedditData(CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD)

base_url = "https://oauth.reddit.com/r/"
subReddits = [
  "ksi",
  "PewdiepieSubmissions",
  "W2S",
  "Sidemen"
]

elasticData = redditData.fetchData(base_url, subReddits)

print(elasticData)


# Save as JSON
out_file = open("redditData.json", "w") 
json.dump(elasticData, out_file) 
out_file.close() 
print("JSON Created!")
