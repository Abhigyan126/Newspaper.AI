from getnews import NewsFetcher
import json

news = NewsFetcher
data = news.get_fake_news()
data = news.clean_json(data)

print(data['data'])
