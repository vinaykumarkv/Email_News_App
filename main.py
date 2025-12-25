import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("MY_API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-11-25&sortBy=publishedAt&apiKey={api_key}"
# Define headers to mimic a common web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Pass the headers to the requests.get function
request = requests.get(url, headers=headers)
content = request.text
print(content)
