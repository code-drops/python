# extracting movie details from imdb

import bs4
import urllib.request as url
import lxml

# input movie name
moviename = input("Enter movie name : ")
moviename=moviename.split()
moviename="+".join(moviename)

# url of movie
path = "https://www.imdb.com/find?ref_=nv_sr_fn&q="+moviename

# opening the above url that outputs the list of movie
http = url.urlopen(path)
page = bs4.BeautifulSoup(http,"lxml")

# finding the tag
td = page.find('td',class_="result_text")

# finding the href attribute of the <a> that provides the actual path of the movie
href=td.find('a').attrs['href']

# new path
newpath="https://www.imdb.com"+href

# opening new path
http = url.urlopen(newpath)
page = bs4.BeautifulSoup(http,"lxml")

# fetching the title of the movie
title = page.find('div',class_="title_wrapper")

# formatting of the title
title=title.text.replace("\n"," ")
title=title.split()
title=" ".join(title)
print("Title : "+title)

# fetching other details
summary=page.find('div',class_="summary_text")
summary=summary.text
summary=summary.split()
summary=" ".join(summary)
print("Summary : "+ summary)

data = page.findAll('div',class_="credit_summary_item")
for item in data:
    item = item.text
    item = item.split()
    item = " ".join(item)
    print(item)