# Le Monde - scrape.py - Scrape le bloc "En Continu" de la frontpage
# de Le monde.

import bs4
import requests
import csv
import os.path

source = requests.get('http://www.lemonde.fr/').text
soup = bs4.BeautifulSoup(source, 'lxml')

bloc = soup.find('ul', class_='liste_horaire')

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

    filename = 'PATH_.CSV'
    fileEmpty = os.stat(filename).st_size == 0

    with open(filename, 'a') as csv_file:
        headers = ['Hours', 'Titles', 'Links']

        csv_writer = csv.DictWriter(csv_file, fieldnames=headers,
                                    delimiter='\t')
        if fileEmpty:
            csv_writer.writeheader()    # file doesn't exist, write header
        csv_writer.writerow({'Hours': hours, 'Titles': titles, 'Links': lm_link})

    csv_file.close()
