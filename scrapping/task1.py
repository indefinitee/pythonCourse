from urllib.request import urlopen
from bs4 import BeautifulSoup

# Напишите программу для получения названий последних статей из блога:

url = 'https://www.oreilly.com/radar/'
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')

articles = set()

for header in soup.find_all('h2', class_='post-title'):
    a = header.get_text()
    if a is not None:
        articles.add(a)

print('Заголовки: ', [header for header in articles])
