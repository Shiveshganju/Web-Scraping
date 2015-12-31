## Script which returns top 5 search results in Bing when searching for Star Wars

import requests

from bs4 import BeautifulSoup
## Bing searches for star wars URL
k,t=0,0
url=["http://www.bing.com/search?q=star+wars&qs=n&form=QBLH&pq=star+wars&sc=9-9&sp=-1&sk=&cvid=5F5D9F00DBF14B9D8FFFF0CEFB0B1E77","https://in.search.yahoo.com/search?p=star+wars&fr=yfp-t-704"]
for i in range(0,2):
 r=requests.get(url[1])
 soup=BeautifulSoup(r.content,"lxml")

 if i==0:
  for k in range(0,5):
   for items in soup.find_all('li',{'class':'b_algo'})[k]:
    for b in items.find_all("a"):
     print "("+str(k+1)+")"+" "+b.text+"       "+b.get('href')
 
 if i==1:
  for t in range(0,5):
   for items in soup.find_all('h3',{'class':'title'})[t]:
    print "("+str(t+5)+")"+" "+items.text+"       "+items.get('href')


