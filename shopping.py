# This Script helps me in selecting products from 3 websites Flipkart, Amazon, Snapdeal as I shop on these sites only. Gives me the minimum price of the product on the 3 websites
# I have chosen Relevancy as the filter as the already sorted elements in these websites dont show products that are relevant 
# Internet connection is a MUST
import requests
from bs4 import BeautifulSoup
from gi.repository import Notify

Notify.init('my app')
a=[]
b=[]
c=[]

products=list(raw_input("What product do you want to search for?\n"))

##Helps in solving the keyword problem
for i in range(0,len(products)):
 if products[i]==' ':
  products[i]='+'


product="".join(products)

##URL of the websites Flipkart, Snapdeal, Amazon
url=["http://www.flipkart.com/search?q="+str(product)+"&as=off&as-show=off&otracker=start","http://www.snapdeal.com/search?keyword="+str(product)+"&santizedKeyword=&catId=&categoryId=&suggested=false&vertical=&noOfResults=48&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&url=&utmContent=&dealDetail=&sort=rlvncy"
,"http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="+str(product)]


for t in range(0,3):
 r=requests.get(url[t])
 
 if t==0:
  soup=BeautifulSoup(r.content,"lxml") 
  for i in range(0,10):
   price=list(str(soup.find_all('div',{'class':'pu-final'})[i].text)[5:len(str(soup.find_all('div',{'class':'pu-final'})[i].text))-1]) 
   if len(price)>3:
    price.remove(',')
   a.append(int("".join(price)))


  prices= min(float(s) for s in a)
  

  z = a.index(prices)
    
 elif t==1:
  soup=BeautifulSoup(r.content,"lxml")    
## the range can be increased. I have kept it to 10 as the relevancy decreases as range increases 
  for i in range(0,10):
   price2=list(soup.find_all('span',{'class':'product-price'})[i].text[5:])
  
   if len(price2)>3:
    price2.remove(',')
   b.append(int("".join(price2)))

  prices2= min(float(s2) for s2 in b)
  
  z2=b.index(prices2)
 
 elif t==2:
  
  soup=BeautifulSoup(r.content,"lxml")

  for i in range(0,10):

   price3=list(soup.find_all('span',{'class':'a-size-base a-color-price s-price a-text-bold'})[i].text[2:len(soup.find_all('span',{'class':'a-size-base a-color-price s-price a-text-bold'})[i].text)-3])

   if len(price3)>3:

    price3.remove(',')

   c.append(int("".join(price3)))


  prices3= min(float(s3) for s3 in c)
  

  z3=c.index(prices3)


if prices<prices2 and prices<prices3:
 soup=BeautifulSoup(requests.get(url[0]).content,"lxml")

## This command will show the desktop notifications 
 n=Notify.Notification.new(soup.find_all('div',{'class':'pu-title fk-font-13'})[z].text+"    "+str(prices)+"\n"+"At Flipkart. Link given in the terminal")

 n.show()

elif prices2<prices and prices2<prices3:

 soup=BeautifulSoup(requests.get(url[1]).content,"lxml")

 n=Notify.Notification.new(soup.find_all('p',{'class':'product-title'})[z2].text+"    "+str(prices2)+"\n"+"At SnapDeal. Link given in the terminal")

 n.show()

else:

 n=Notify.Notification.new(soup.find_all('h2',{'class':'a-size-medium a-color-null s-inline s-access-title a-text-normal'})[z3].text+"    "+str(prices3)+"\n"+"At Amazon. Link given in the terminal")

 n.show()


 


