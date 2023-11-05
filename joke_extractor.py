from bs4 import BeautifulSoup
from zenrows import ZenRowsClient
import os

api_key = os.getenv('ZENROWS_API_KEY')
# Initialize the ZenRows client with my API key
client = ZenRowsClient(api_key)

# URL of the page to scrape
url = "https://parade.com/968666/parade/chuck-norris-jokes/"

# Parameters to enable JavaScript rendering, anti-bot measures, and premium proxies
params = {"js_render": "true", "antibot": "true", "premium_proxy": "true"}


def extract_joke(joke_number: int) -> str:
    # Make the request through ZenRows
    response = client.get(url, params=params)

    # Check if the request was successful
    if response.status_code != 200:
        return f"Failed to retrieve jokes, status code: {response.status_code}"

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    jokes = soup.select('ol > li')
    joke_index = joke_number - 1
    if 0 <= joke_index < len(jokes):
        return jokes[joke_index].get_text().strip()
    else:
        return "Joke number is out of range."
