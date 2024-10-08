from getnews import NewsFetcher
import json

news = NewsFetcher
data = news.get_fake_news()

print(len(data['data']))