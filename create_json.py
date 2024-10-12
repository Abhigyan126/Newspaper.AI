import json
from getnews import NewsFetcher

class NewsPipeline:
    def __init__(self):
        self.data = NewsFetcher.get_fake_news()
        self.results = []
        self.count = 0

    def process_news(self):
        for article in self.data:
            published_at = article["published_at"]
            category = article["category"]
            title = article["title"]
            description = article["description"]
            url = article["url"]
            content = NewsFetcher.get_text_from_url(url)
            generated_text = NewsFetcher.generate(title, content, description)
            title, news = NewsFetcher.extract_tittle(generated_text)
            print(self.count)
            self.count += 1

            news_entry = {
                "title": title,
                "description": description,
                "url": url,
                "published_at": published_at,
                "category": category,
                "news": news
            }
            self.results.append(news_entry)

    def save_to_json(self, file_name="processed_news.json"):
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=4, ensure_ascii=False)

    def get_results(self):
        return self.results

def main():
    pipeline = NewsPipeline()
    pipeline.process_news()
    pipeline.save_to_json()
    processed_news = pipeline.get_results()
    for news in processed_news:
        print(json.dumps(news, indent=4))

if __name__ == "__main__":
    main()
