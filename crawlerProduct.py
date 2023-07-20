import requests
from bs4 import BeautifulSoup
import json
import certifi
from urllib.parse import urljoin

requests.packages.urllib3.disable_warnings()
verify_ssl = False



def get_subpage_links(url):
    response = requests.get(url, verify=False)  # Add verify=False to bypass SSL certificate verification
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Modify the selector to find the links to sub-pages or documents
        subpage_links = [link['href'] for link in soup.find_all('a', href=True)]  # Update the selector
        return subpage_links
    else:
        print(f"Failed to fetch the page: {url}")
        return []

def scrape_subpage_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Modify the selector to find the content on the sub-pages or documents
        subpage_content = soup.find('div', {'class': 'your-subpage-class'})  # Update the selector
        if subpage_content:
            subpage_text = subpage_content.get_text(separator='\n').strip()
            return subpage_text
        else:
            print(f"Subpage content not found on the page: {url}")
            return None
    else:
        print(f"Failed to fetch the subpage: {url}")
        return None



# ... other functions ...

if __name__ == "__main__":
    product_url = 'https://www.ciena.com/products/converged-packet-optical'
    subpage_links = get_subpage_links(product_url)

    # Remove duplicate URLs using set()
    unique_subpage_links = set(subpage_links)

    all_subpage_content = {}

    for link in unique_subpage_links:
        full_link = urljoin(product_url, link)
        subpage_content = scrape_subpage_content(full_link)
        if subpage_content:
            all_subpage_content[full_link] = subpage_content

    # Save to JSON file
    with open('product_content.json', 'w') as json_file:
        json.dump(all_subpage_content, json_file, indent=4)
