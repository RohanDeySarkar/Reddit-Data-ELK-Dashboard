![](https://github.com/RohanDeySarkar/Reddit-Data-ELK-Dashboard/blob/master/Dashboard%20Screenshot.png?raw=true)

1. Create App to get client id and secret https://www.reddit.com/prefs/apps
2. Run getRedditData.py [Fetch data & store in JSON]
3. Run client.py & logstashServer.conf [client & logstash server]
4. Check data on Elastic 
(PUT /redditdataset, GET /redditdataset/_search, DELETE /redditdataset)
5. Dashboard
