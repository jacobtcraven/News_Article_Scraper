import requests
from bs4 import BeautifulSoup


URL = "https://sports.yahoo.com/kyle-shanahans-49ers-lost-super-160726345.html"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
"""this HEADER helps to access websites that don't like web scraping."""

def read_urls(filename):
    """Read URLs from a .txt file"""
    with open(filename, 'r') as file:
        urls = file.readlines()
    urls = [url.strip() for url in urls]
    return urls


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    lookUp = BeautifulSoup(response.text, 'html.parser')
    article = lookUp.find("div", class_='caas-body')
    return article.get_text()


def write_to_file(article, filename):
    """Write the article to a .txt file"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(article)

def newline(article):
    """Add a new line for every 20 words in the article"""
    article = article.split()
    for i in range(len(article)):
        if i % 20 == 0:
            article.insert(i, '\n')
    return ' '.join(article)


if __name__ == '__main__':
    urls = read_urls('urls.txt')
    counter = 1
    for URL in urls:
        source = scrape(URL)
        # print(URL)
        formatted = newline(source)
        write_to_file(formatted, f'article{counter}.txt')
        counter += 1
