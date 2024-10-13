#Newspaper.AI
 
News Processing Pipeline 
Implementation - https://newspaper-ai-two.vercel.app/
Frontend Implementation - https://github.com/Abhigyan126/Newspaper.ai-React

This repository contains a Python-based pipeline that fetches news articles, processes them, and updates the results to a GitHub repository. The code uses classes like `NewsFetcher` and `GitHubRepoManager` to handle news fetching and GitHub repository updates, respectively.

## Features

- **Fetch News Articles**: Retrieves a list of news articles using the `NewsFetcher` class.
- **Process Articles**: Extracts content, generates summaries, and stores results in a structured format.
- **Progress Indicator**: Shows real-time progress of news processing in the terminal.
- **Save Processed News**: Stores the processed news articles in a JSON file (`processed_news.json`).
- **Update GitHub Repository**: Automatically commits and pushes changes to a specified GitHub repository using the `GitHubRepoManager`.

## Project Structure

```bash
.
├── getnews.py               # Contains the NewsFetcher class for fetching and processing news content.
├── update_github.py         # Contains the GitHubRepoManager class for managing the GitHub repo.
├── main.py                  # The main script that runs the pipeline.
├── src/
│   └── processed_news.json   # The output JSON file where processed news will be saved.
└── README.md                # This file.
```

## Setup Instructions

### Prerequisites

- **Python 3.8 or higher** installed.
  
- **getnews.py** and **update_github.py** should be properly configured:

  - `getnews.py` handles fetching news from a source and processing content.
  - `update_github.py` should have the necessary logic for interacting with GitHub (e.g., authentication, repository access).

### Installation

1. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Fetch and Process News**: The script fetches news articles, processes them, and updates the GitHub repository.

   Run the main script using:

   ```bash
   python main.py
   ```

2. **Saving Results**: The processed articles will be saved in `src/processed_news.json`.

3. **GitHub Repository Update**: The script will automatically update the repository after processing the news.

### Customization

- **Modifying News Sources**: To change the news source or the way content is fetched, modify the `getnews.py` file. This file defines how articles are fetched, extracted, and processed.
  
- **GitHub Configuration**: To change the GitHub update logic, modify the `update_github.py` file to suit your repository structure and credentials.

### Example Output

An example of the JSON output:

```json
[
    {
        "title": "Sample News Title",
        "url": "https://example.com/news/1",
        "published_at": "2024-10-01",
        "category": "Technology",
        "news": "Generated summary of the news article."
    },
    ...
]
```

## Contributions

Feel free to fork this repository, submit issues, or open pull requests for any improvements or new features.

## License

This project is licensed under the MIT License.
