import requests
from bs4 import BeautifulSoup


def name_of_computer_science(url):
    res = requests.get(url)
    header = BeautifulSoup(res.text, "html.parser")
    soup = header.select("td:nth-child(2)")
    # for item in soup:
    #     print(item.get_text())
    res = [item.get_text() for item in soup]
    return res


def date_of_the_computer_science(url):
    res = requests.get(url)
    header = BeautifulSoup(res.text, "html.parser")
    soup = header.select("td:nth-child(1)")
    # for item in soup:
    #     print(item.get_text())
    res = [item.get_text() for item in soup]
    return res


def find_books_of_computer_science(name):
    url = f"https://www.goodreads.com/search?q={name.replace(' ', '+')}"
    res = requests.get(url)
    header = BeautifulSoup(res.text, "html.parser")
    soup = header.find("a", class_="bookTitle")
    if soup:
        book_title = soup.text.strip()
        book_url = "https://www.goodreads.com/" + soup["href"]
        return book_title, book_url
    else:
        return "No book found", " "


def main():
    info = "https://en.wikipedia.org/wiki/List_of_pioneers_in_computer_science"
    names = name_of_computer_science(info)
    for name in names:
        print(f"Name: {name}")
        book_title, book_url = find_books_of_computer_science(name)
        print(f"Book title: {book_title}")
        print(f"Book url: {book_url}")
    else:
        print("No book found")
    print()


main()
