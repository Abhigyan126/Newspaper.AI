import http.client
import urllib.parse
import json
import html
import requests
from llm import LLM
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


class NewsFetcher:
    @staticmethod
    def get_news():
        try:
            load_dotenv()
            apikey_for_news = os.getenv('apikey_for_news')
            conn = http.client.HTTPConnection('api.mediastack.com')

            params = urllib.parse.urlencode({
                'access_key': apikey_for_news,
                'countries': 'in',
                'categories': '-general,-sports',
                'sort': 'published_desc',
                'limit': 100,
            })

            conn.request('GET', '/v1/news?{}'.format(params))
            res = conn.getresponse()
            data = res.read()

            # Load the JSON response
            json_data = json.loads(data.decode('utf-8'))
            return json_data['data']

        except Exception as e:
            print(f"Error occurred: {e}")
            return None

        finally:
            conn.close()
    
    @staticmethod
    def get_fake_news(filename='news_data.json'):
        try:
            with open(filename, 'r') as json_file:
                data = json.load(json_file)
            print(f"Data successfully loaded from {filename}")
            return data["data"]
        except FileNotFoundError:
            print(f"{filename} not found. Please fetch news data first.")
            return None
        except Exception as e:
            print(f"Error occurred while loading data: {e}")
            return None
    @staticmethod
    def clean_json(data):
        """
        Recursively clean and filter all elements in the JSON data.
        - Converts Unicode to readable format.
        - Unescapes HTML entities.
        - Replaces None values with 'Unknown'.
        """
        def clean_value(value):
            if isinstance(value, str):
                return html.unescape(value)
            elif value is None:
                return "Unknown"
            else:
                return value

        if isinstance(data, dict):
            return {key: NewsFetcher.clean_json(value) for key, value in data.items()}

        elif isinstance(data, list):
            return [NewsFetcher.clean_json(item) for item in data]

        else:
            return clean_value(data)
    @staticmethod
    def get_text_from_url(url):
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract all text from the webpage
            all_text = soup.get_text(strip=True)
            # Optional: You can split the text into lines or paragraphs for better formatting
            lines = all_text.splitlines()
            # Remove empty lines
            formatted_text = [line for line in lines if line]
            return formatted_text
        else:
            return response.status_code
    @staticmethod
    def generate(tittle, message, description):
        prompt = f"you are journalist, your job is to write short information dense articles on topic and content provided to you,there maybe many non essential information included filter them and translate to english if required here is tittle: {tittle}, here is discription: {description}, here is content: {message}"
        llm = LLM()
        return llm.model(prompt)
    @staticmethod
    def extract_tittle(markdown_text):
        lines = markdown_text.splitlines()
        title = ''
        content = ''
        for line in lines:
            if line.startswith('##'):
                title = line.lstrip('##').strip()
            else:
                content += line + '\n'
        content = content.strip()
        return title, content

