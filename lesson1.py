import requests
from bs4 import BeautifulSoup


def main():
    link = 'https://wordpress.org'
    print(get_data(get_html(link)))


def get_html(link):
    response = requests.get(link)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('h1').text
    return h1


if __name__ == '__main__':
    main()
