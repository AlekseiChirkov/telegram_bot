import requests
import pandas as pd
import csv

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
    """Writing data in .csv file"""
    headers = get_headers()
    headers = {'headers': headers}
    headers = pd.DataFrame.from_dict(headers, orient='index')
    headers = headers.replace(r'\n', ' ', regex=True)
    headers = headers.replace(r'\r', ' ', regex=True)
    headers = headers.replace(r'\t', ' ', regex=True)
    headers = headers.replace(r'\\t', ' ', regex=True)
    headers = headers.replace(r'       ', ' ', regex=True)
    headers = headers.replace(r'      ', ' ', regex=True)

    paragraphs = get_paragraphs()
    paragraphs = {'paragraphs': paragraphs}
    paragraphs = pd.DataFrame.from_dict(paragraphs, orient='index')
    paragraphs = paragraphs.replace(r'\n', ' ', regex=True)
    paragraphs = paragraphs.replace(r'\r', ' ', regex=True)
    paragraphs = paragraphs.replace(r'\t', ' ', regex=True)
    paragraphs = paragraphs.replace(r'\\t', ' ', regex=True)
    paragraphs = paragraphs.replace(r'       ', ' ', regex=True)
    paragraphs = paragraphs.replace(r'      ', ' ', regex=True)

    return headers.to_csv('headers.csv', index=False), paragraphs.to_csv('paragraphs.csv', index=False)


dataframe()
