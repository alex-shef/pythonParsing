import requests
from bs4 import BeautifulSoup
import re

LINK = "https://premierliga.ru/tournament-table/"


def main():
    link = LINK
    print(get_data(get_html(link)))


def get_html(link):
    response = requests.get(link)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('div', class_=('stats-tournament-table')).find(
        'table').find_all('tr')
    for tr in trs:

        position = tr.find_all('td', class_='place')
        for i in position:
            positions = i.text.strip()+'  '
            # print(positions)

        club = tr.find_all('td', class_='club')
        for i in club:
            clubs = i.text.replace('\n', '')
            # print(clubs)

        goal = tr.find_all('td', class_='dark-blue goals')
        for i in goal:
            goals_plus = i.find('span', class_='green').get_text()
            goals_minus = i.find('span', class_='red').get_text()
            # print(goals_plus,'-',goals_minus)

        point = tr.find_all("p", {"class": "points"})
        for i in point:
            points = i.text.replace('\n', '')
            # print(points)

            print(positions, clubs, goals_plus, 'Голов Забито', '-',
                  goals_minus, 'Голов Пропущено', points, 'Очков')


# return trs

if __name__ == '__main__':
    main()
