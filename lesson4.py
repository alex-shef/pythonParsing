import requests
from bs4 import BeautifulSoup
import csv


def refinde(s):
    str_ = s.split()[0]
    return str_.replace(',', '')


def write_csv(data):
    with open('pagination4.csv', 'w') as f:
        recorder = csv.writer(f)

        recorder.writerow((data['h3'],
                           data['a'],
                           data['rating']
                           ))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find('main', class_='site-main').find_all('article')
    for article in articles:
        h3 = article.find('h3').get_text()
        a = article.find('h3').find('a').get('href')
        rating = article.find('span', class_='rating-count').find(
            'a').get_text()

        data = {'h3': h3,
                'a': a,
                'rating': rating}
        write_csv(data)
        print(h3, a, refinde(rating))


def get_html(url):
    r = requests.get(url)
    return r.text


def main():
    for i in range(1, 26):
        url = f'https://wordpress.org/plugins/browse/blocks/page/{i}'
        print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
