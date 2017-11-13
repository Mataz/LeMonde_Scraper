# Le Monde - scraper.py - Scrape le bloc "En Continu" de la frontpage
# de Le monde.

import bs4
import requests
import csv

source = requests.get('http://www.lemonde.fr/').text
soup = bs4.BeautifulSoup(source, 'lxml')
bloc = soup.find('ul', class_='liste_horaire')

csv_file = open('lemonde_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Hours', 'Titles', 'Links'])

for news in bloc.find_all('li'):

    hours = news.span.text
    print(hours)

    try:
        titles = news.find('a').text
    except Exception as e:
        titles = None

    print(titles)

    try:
        links = news.find('a')['href']
        lm_link = f'https://www.lemonde.fr/{links}'
    except Exception as e:
        lm_link = None

    print(lm_link)

    print()

    csv_writer.writerow([hours, titles, lm_link])

csv_file.close()
