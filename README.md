# Newspaper.AI

# News Processing Pipeline

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
