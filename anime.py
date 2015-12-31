##Script which searches for top 5 upcoming animes from myanimelist.net

import requests

from bs4 import BeautifulSoup
##URL of myanimelist.net
url="http://myanimelist.net/topanime.php?type=upcoming"

r=requests.get(url)

soup=BeautifulSoup(r.content,"lxml")

for i in range(0,10):

 for item in soup.find_all('td',{'class':'borderClass bgColor2'})
[i].find_all('a',{'class':'hoverinfo_trigger'}):

  print "("+str((i+1)/2)+") " +item.text

