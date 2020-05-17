# extracting names and prices of various mobile phones from flipkart

import bs4
import urllib.request as url
import lxml

http=url.urlopen("https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
page=bs4.BeautifulSoup(http,"lxml")
div=page.findAll("div",class_="_3wU53n")
price=page.findAll("div",class_="_1vC4OE _2rQ-NK")

for i in range(len(div)):
    print(div[i].text)
    print(price[i].text)
    print("-------------------")
