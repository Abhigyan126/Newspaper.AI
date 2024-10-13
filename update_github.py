import os
from github import Github
from dotenv import load_dotenv
import base64

# Load environment variables from .env file
load_dotenv()

class GitHubRepoManager:
    def __init__(self):
        # Load variables from the .env file
        self.token = os.getenv("GITHUB_TOKEN")
        self.repo_name = os.getenv("REPO_NAME")
        self.file_path = os.getenv("FILE_PATH")

        # Initialize the GitHub API with the token
        self.g = Github(self.token)
        self.repo = self.g.get_repo(self.repo_name)

    def get_branch(self):
        branches = self.repo.get_branches()
        for branch in branches:
            print(f"Branch: {branch.name}")
    
    def update_file(self):
        # Read the local file content
        with open(self.file_path, 'r') as local_file:
            local_content = local_file.read()

        try:
            # Get the file content from the GitHub repo
            file_content = self.repo.get_contents(self.file_path)
            sha = file_content.sha
            encoded_content = file_content.content
            decoded_content = base64.b64decode(encoded_content).decode("utf-8")
        except Exception as e:
            print(f"Error getting file: {e}")
            sha = None

        if sha:
            try:
                # Update the file in the repo
                self.repo.update_file(
                    self.file_path,
                    "Update file content through API",
                    local_content,
                    sha,
                    branch="main"
                )
                print("File updated successfully.")
            except Exception as e:
                print(f"Error updating file: {e}")
        else:
            print("File not found.")

if __name__ == "__main__":
    manager = GitHubRepoManager()
    manager.get_branch()
    manager.update_file()
