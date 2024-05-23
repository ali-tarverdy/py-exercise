import requests
from bs4 import BeautifulSoup


def authors_names(url):
    res = requests.get(url)
    header = BeautifulSoup(res.content, "html.parser")
    # Using find() with proper tag and attributes
    name = header.select("#content-collapsible-block-0")
    print(name)


authors_names("https://en.m.wikipedia.org/wiki/List_of_authors_by_name:_T")
