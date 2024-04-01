import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/88.0.4324.182 Safari/537.36"}

data = requests.get("https://www.imdb.com/find/?q=thriller&s=tt&ref_=fn", headers=headers)
soup = BeautifulSoup(data.content, 'html.parser')
#print(soup.prettify())
movies = soup.find('ul',{'class': 'ipc-metadata-list ipc-metadata-list--dividers-after sc-17bafbdb-3 WTcPP ipc-metadata-list--base'})
#print(movies.prettify())
rows = movies.findAll('li')
#print(rows)
for row in rows:
    rowData = row.findAll('div')
    if len(rowData) >= 3:
        print(rowData[2].div.a.text)
        subUrl = rowData[2].div.a['href']
        subsData = requests.get(f'https://www.imdb.com{subUrl}', headers=headers)
        childSoup = BeautifulSoup(subsData.content, 'html.parser')
        #print(childSoup.prettify())
        if  childSoup.findAll('ul', {'class':'ipc-metadata-list ipc-metadata-list--dividers-all sc-f5ef05d0-1 WmMVu ipc-metadata-list--base'}):
            genre = childSoup.findAll('ul', {'class':'ipc-metadata-list ipc-metadata-list--dividers-all sc-f5ef05d0-1 WmMVu ipc-metadata-list--base'})
            print(genre)
        else:
            print('not found')



