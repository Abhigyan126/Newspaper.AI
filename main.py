import json
from getnews import NewsFetcher
from update_github import GitHubRepoManager

class NewsPipeline:
    def __init__(self):
        self.data = NewsFetcher.get_fake_news()
        self.manager = GitHubRepoManager()

        self.results = []

    def process_news(self):
        for article in self.data:
            title = article["title"]
            description = article["description"]
            url = article["url"]
            content = NewsFetcher.get_text_from_url(url)
            generated_text = NewsFetcher.generate(title, content, description)

            news_entry = {
                "title": title,
                "description": description,
                "url": url,
                "generated_text": generated_text
            }
            self.results.append(news_entry)

    def get_results(self):
        return self.results

def main():
    pipeline = NewsPipeline()
    pipeline.process_news()
    processed_news = pipeline.get_results()

    print(processed_news)

if __name__ == "__main__":
    main()
