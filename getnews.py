import http.client
import urllib.parse
import json

class NewsFetcher:
    @staticmethod
    def get_news():
        try:
            conn = http.client.HTTPConnection('api.mediastack.com')

            params = urllib.parse.urlencode({
                'access_key': 'api_key_ur',
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
            return json_data

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
            return data
        except FileNotFoundError:
            print(f"{filename} not found. Please fetch news data first.")
            return None
        except Exception as e:
            print(f"Error occurred while loading data: {e}")
            return None

        
