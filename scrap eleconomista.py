

from bs4 import BeautifulSoup
import requests



#scrapea títulos del diario el economista argentina
website = 'https://eleconomista.com.ar'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())
##acabamos de traer la web en html


titulos = 'Títulos: \n\n'

k=1
while k < 4:
    tits1 = soup.find_all('h'+str(k), class_='tit')
    for _tits1 in tits1:
        stits1 = _tits1.find_all('a')
        for _stits1 in stits1:
            sstits1 = _stits1.find_all('title')
            for _sstits1 in stits1:
                #print(_sstits1.text)   #printea en consola
                titulos = titulos + _sstits1.text + '\n\n'
    k = k+1


with open(f'Títulos El Economista.txt', 'w') as file:
          file.write(titulos)

