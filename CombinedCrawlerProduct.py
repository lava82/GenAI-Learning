import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib3
import json
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Gets the link from the Cinea
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

# Scraping the content of the link
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
# Scraping the product content page
# Scraping the product content page
# Scraping the product content page
import requests
# ... (other import statements and functions)

# Scraping the product content page
def scrape_subpage_content_Product(url):
    if url.startswith('tel:') or url.startswith('mailto:'):
        print(f"Skipping telephone or email link: {url}")
        return None

    response = requests.get(url, verify=False)  # Disable SSL certificate verification
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Modify the selector to find the content on the sub-pages or documents
        subpage_content = soup.find('div', {'class': 'your-subpage-class'})  # Update the selector
        if subpage_content:
            subpage_text = subpage_content.get_text(separator='\n').strip()
            return subpage_text
        else:
            print(f"Subpage content Product found on the page: {url}")
            return None
    else:
        print(f"Failed to fetch the subpage: {url}")
        return None


# After Scraping the product Content link to the Sub pages to the URL
def get_subpage_links_product(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Modify the selector to find the links to sub-pages or documents
        subpage_links = [link['href'] for link in soup.find_all('a', href=True)]  # Update the selector
        return subpage_links
    else:
        print(f"Failed to fetch the page: {url}")
        return []


# Main function executes the link of the Entire Cinea websites, Product Link of subpages and the documents
if __name__ == "__main__":
    base_url = 'https://www.ciena.com/insights'
    article_links = get_article_links(base_url)

    all_article_content = {}

    for link in article_links:
        full_link = urljoin(base_url, link)
        article_content = scrape_article_content(full_link)
        if article_content:
            all_article_content[full_link] = article_content

    product_url = 'https://www.ciena.com/products/converged-packet-optical'
    subpage_links = get_subpage_links_product(product_url)

    all_subpage_content = {}

    ALL_LINKS = article_links + subpage_links

    # Filter out non-URLs using regular expression
    valid_url_pattern = re.compile(r'^https?://\S+$')
    ALL_LINKS = [link for link in ALL_LINKS if valid_url_pattern.match(link)]

    for link in ALL_LINKS:
        full_link = urljoin(product_url, link)
        if not link.startswith('tel:'):
            full_link = urljoin(product_url, link)
        subpage_content = scrape_subpage_content_Product(full_link)
        if subpage_content:
            all_subpage_content[full_link] = subpage_content

    # Do something with all_article_content, like saving it to a file
    # can save it to a JSON file:

    import json

    with open('ciena_insights_articles.json', 'w') as json_file:
        json.dump(all_article_content, json_file, indent=4)

    # Save all_subpage_content to a JSON file
    with open('product_content.json', 'w') as json_file:
        json.dump(all_subpage_content, json_file, indent=4)