import requests
from bs4 import BeautifulSoup


def get_html():
    """Getting html page content"""

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
    url = 'https://честныйзнак.рф/vopros-otvet/'
    session = requests.Session()
    response = session.get(url, headers=headers)
    page = response.text
    soup = BeautifulSoup(page, 'html.parser')

    return soup


def get_headers():
    """Getting headers from categories"""
    soup = get_html()
    titles = []
    for i in soup.find_all('i'):
        header = str(i.text)
        titles.append(header.strip())

    return titles


def get_paragraphs():
    """Getting paragraphs from categories"""
    soup = get_html()
    paragraphs = []
    for i in soup.findAll('div', {'class': 'faq-list1__hide'}):
        p = str(i.text)
        paragraphs.append(p.strip())
    return paragraphs
