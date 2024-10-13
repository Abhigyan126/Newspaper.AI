import json
import sys
from getnews import NewsFetcher
from update_github import GitHubRepoManager

class NewsPipeline:
    def __init__(self):
        self.data = NewsFetcher.get_news()
        self.results = []
        self.count = 0
        self.total_articles = len(self.data)

    def display_progress(self, progress, max_progress=100):
        bar_length = 40  # Length of the progress bar
        block = int(round(bar_length * progress / max_progress))
        progress_bar = f"[{'#' * block}{'.' * (bar_length - block)}] {progress}%"
        sys.stdout.write(f"\r{progress_bar} - Processing {self.count}/{self.total_articles} | Current News: {self.current_title}")
        sys.stdout.flush()

    def process_news(self):
        for article in self.data:
            published_at = article["published_at"]
            category = article["category"]
            title = article["title"]
            description = article["description"]
            url = article["url"]
            
            # Fetching the content
            content = NewsFetcher.get_text_from_url(url)
            generated_text = NewsFetcher.generate(title, content, description)
            title, news = NewsFetcher.extract_tittle(generated_text)
            self.current_title = title
            self.count += 1
            progress = (self.count / self.total_articles) * 100
            self.display_progress(progress)

            news_entry = {
                "title": title,
                "url": url,
                "published_at": published_at,
                "category": category,
                "news": news
            }
            self.results.append(news_entry)

    def save_to_json(self, file_name="src/processed_news.json"):
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=4, ensure_ascii=True)

    def get_results(self):
        return self.results

def main():
    manager = GitHubRepoManager()

    pipeline = NewsPipeline()
    pipeline.process_news()
    pipeline.save_to_json()
    
    manager.update_file()

if __name__ == "__main__":
    main()
