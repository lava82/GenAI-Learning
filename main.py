import requests

def make_get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.content.decode("utf-8"))
    else:
        print("Request failed with status code:", response.status_code)

# Example usage
url = "https://www.ciena.com"
make_get_request(url)
