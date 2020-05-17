# extracting name of folder from github

import bs4
import urllib.request as url

http = url.urlopen("https://github.com/ravi4all/PythonJulyEve_19/blob/master/Crawl-1.py")

page = bs4.BeautifulSoup(http, 'lxml')
div = page.find("span", class_='js-path-segment')

print(div.text)
