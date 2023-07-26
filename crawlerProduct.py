import re
import requests
from bs4 import BeautifulSoup
import textwrap

def ExtractTextFromWebpage(url):
    response = requests.get(url)
    html_page = BeautifulSoup(response.text, "html.parser")
    all_words = set()  # Use a set to store unique words

    for element in html_page.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'li']):
        text = element.get_text().strip()
        if text:
            text = re.sub(r'[^\w\s]', '', text)
            text = text.lower()
            words = text.split()

            for word in words:
                all_words.add(word)  # Add each word to the set

    return ' '.join(all_words)  # Join unique words back into a string

def GetAllPage(url, visited_urls=None):
    if visited_urls is None:
        visited_urls = set()

    internal_urls = set()
    external_urls = set()

    response = requests.get(url)
    html_page = BeautifulSoup(response.text, "html.parser")

    all_urls = html_page.findAll("a")

    for link in all_urls:
        href = link.get('href')
        if href:
            if href not in visited_urls:
                visited_urls.add(href)
                if "www.ciena.com/products/" in href:
                    internal_urls.add(href)
                else:
                    external_urls.add(href)
    return internal_urls, external_urls

url = "https://www.ciena.com/products/converged-packet-optical/"
internal_urls, external_urls = GetAllPage(url)

print("Internal URLs:")
for link in internal_urls:
    print(link)

print("\nExternal URLs:")
for link in external_urls:
    print(link)

# Extract text related to "converged-packet-optical" from the provided URL
extracted_texts = []
for url in internal_urls:
    extracted_text = ExtractTextFromWebpage(url)
    extracted_texts.append(extracted_text)

print("\nExtracted Texts:")
for i, text in enumerate(extracted_texts, 1):
    print(f"Text {i}:")
    for line in textwrap.wrap(text, width=80):
        print(line)
    print()
print('done')