#!/usr/bin/python3
import urllib.request
import bs4

url = "https://www.savoir-inutile.com/"

page = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(page, "html.parser")
phrase = soup.find("h2", {"id": "phrase"})

print(phrase.text)
