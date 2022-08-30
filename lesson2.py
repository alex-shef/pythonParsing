import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def refinde(str_):
    s = str_.split(' ')[0]
    return s.replace(',', '')


def write_csv(data):
    with open('listplugins2.csv', 'w') as f:
        recorder = csv.writer(f)

        recorder.writerow((data['h3'],
                           data['link'],
                           data['rating']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('article')
    for article in articles:
        h3 = article.find('h3', class_='entry-title').text
        link = article.find('h3', class_='entry-title').find('a').get('href')
        rating = article.find('div', class_="plugin-rating").find('span',
                                     class_="rating-count").find('a').text
        rating = refinde(rating)

        data = {'h3': h3,
                'link': link,
                'rating': rating}
        write_csv(data)


def main():
    url = 'https://wordpress.org/plugins'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
