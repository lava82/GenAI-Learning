import requests
from bs4 import BeautifulSoup

url = 'https://www.ciena.com/insights/articles'

# Send GET request to the website
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the article links
    article_links = soup.find_all('a', class_='card')

    # Iterate over the article links and extract the title and URL
    for link in article_links:
        title = link.text.strip()
        article_url = link['href']
        print(f"Title: {title}")
        print(f"URL: {article_url}")
        print('---')

else:
    print('Failed to retrieve website content.')
