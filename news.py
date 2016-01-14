## Gives me an update whenever some new news comes along ad checks it after every 5 minutes. News is displayed in form of desktop notifications

import requests,time
from bs4 import BeautifulSoup
from gi.repository import Notify


Notify.init('news')

url="http://timesofindia.indiatimes.com/"

desktop_notif=""

news2=""

print " PRESS CTRL-C TO BREAK "

while(1):

 r=requests.get(url)

 soup=BeautifulSoup(r.content,"lxml")

 for links in soup.find_all('div',{'class':'featured'}):

  for news in links.find_all('h2'):  

   news2=news.text  

 if desktop_notif != news2:   

  desktop_notif=news2

  n=Notify.Notification.new(desktop_notif)

  n.show()

  time.sleep(300)                                           ##Can be changed to increase/decrease the frequency with which it checks the news
  
