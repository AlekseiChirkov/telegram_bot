import requests
import pandas as pd

from bs4 import BeautifulSoup


def get_html():
    """Getting html page content"""
    url = 'https://честныйзнак.рф/vopros-otvet/'
    session = requests.Session()
    response = session.get(url)
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
        p = str(i.get_text().strip())
        paragraphs.append(p)
    return paragraphs


def dataframe():
    headers = get_headers()
    paragraphs = get_paragraphs()
    data = {'headers': headers, 'paragraphs': paragraphs}
    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.replace(r'\n', ' ', regex=True)
    df = df.replace(r'\r', ' ', regex=True)
    df = df.replace(r'\t', ' ', regex=True)
    df = df.replace(r'\\t', ' ', regex=True)
    df = df.replace(r'       ', ' ', regex=True)
    df = df.replace(r'      ', ' ', regex=True)

    return df.to_csv('text.csv', index=False)


text = dataframe()
print(text)
