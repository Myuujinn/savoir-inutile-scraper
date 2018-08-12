#!/usr/bin/python3
import sys
import urllib.request
import bs4

url = "https://www.savoir-inutile.com/"
file_name = "phrases.txt"

def scrape():
    page = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(page, "html.parser")
    phrase = soup.find("h2", {"id": "phrase"})

    return phrase.text


def scrape_all():
    phrase_list = []
    while len(phrase_list) < 500:
        phrase = scrape()
        print("Scraped : ", phrase[:50], "..", sep='')
        if phrase not in phrase_list:
            phrase_list.append(phrase)

    print("Writing", file_name)
    file = open(file_name, "w+")
    for phrase in phrase_list:
        file.write(phrase + "\n")
    file.close()


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--scrape-all":
        scrape_all()
    else:
        print(scrape())


if __name__ == '__main__':
    main()
