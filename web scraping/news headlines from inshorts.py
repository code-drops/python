# program to access the news of any type with the python

import bs4
import urllib.request as url
import lxml

category = ["national","business","sports","world","politics","technology","startup","entertainment","miscellaneous","hatke","science","automobile"]

news = input("Enter news category : ")
chat = True
while chat:
    if news not in category:
        chat = False
        print("Please select valid category")
        break
    else:
        news = news.lower()
        path = "https://www.inshorts.com/en/read/" + news
        http = url.urlopen(path)
        page = bs4.BeautifulSoup(http ,"lxml")
        div = page.find_all("div",class_="news-card-title news-right-box")
        for item in div:
            a = item.find("a", class_="clickable")
            headline = a.text
            headline.replace("\n"," ")
            headline = headline.split()
            headline = " ".join(headline)
            print(headline)
            print("---------------------------")