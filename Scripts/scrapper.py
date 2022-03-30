

import requests

import json

from bs4 import BeautifulSoup

req= requests.get("https://time.com/")

soup = BeautifulSoup(req.content,"html.parser")

data = soup.find('div', attrs = {'class':'partial latest-stories'})

title = data.find_all('li', attrs = {'class':'latest-stories__item'})

details =[]
for a in data.find_all('a', href=True):
    ContentUrl = json.dumps({
    'url': str(a['href']) ,
    "title" : str(a.find('h3', attrs = {'class':'latest-stories__item-headline'}))
})
    details.append(ContentUrl )


   
print((details))





    

