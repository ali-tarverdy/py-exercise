#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import sys

word = sys.argv[1]

url = "https://www.google.com/search?q=%s&source=lnms&tbm=isch" % word

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

try:
    print(soup.find_all("img")[3]["src"])
except:
    print("")

# breakpoint()
