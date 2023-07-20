import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_article_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('a', href=True)  # Modify this selector based on the actual structure of the page
        article_links = [link['href'] for link in articles if 'insights' in link['href']]
        return article_links
    else:
        print(f"Failed to fetch the page: {url}")
        return []


def scrape_article_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Modify the selector based on the actual structure of the article page
        article_element = soup.find('div', {'class': 'article-content'})
        if article_element:
            article_content = article_element.text.strip()
            return article_content
        else:
            print(f"Article content  found on the page: {url}")
            return None
    else:
        print(f"Failed to fetch the article: {url}")
        return None


if __name__ == "__main__":
    base_url = 'https://www.ciena.com/insights'
    article_links = get_article_links(base_url)

    all_article_content = {}

    for link in article_links:
        full_link = urljoin(base_url, link)
        article_content = scrape_article_content(full_link)
        if article_content:
            all_article_content[full_link] = article_content

    # Do something with all_article_content, like saving it to a file or a database
    # For example, you can save it to a JSON file:
    import json

    with open('ciena_insights_articles.json', 'w') as json_file:
        json.dump(all_article_content, json_file, indent=4)


