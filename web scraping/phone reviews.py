import bs4
import urllib.request as url
import lxml

# decalring variables
one = 0
two = 0
three = 0
four = 0
five = 0
count = 0

# loop for traversing pages
for i in range(10):
    # url of the page
    path = "https://www.flipkart.com/realme-c2-diamond-black-16-gb/product-reviews/itmfgwbaahz6ph9j?pid=MOBFFMG3FGAFZYVE"+"&page={}".format(i+1)
    http = url.urlopen(path)
    page = bs4.BeautifulSoup(http,'lxml')
    para = page.find_all('p',class_="_2xg6Ul")              # comments of the user
    rating = page.find_all('div',class_="hGSR34 E_uFuv")    # rating of the user
    for p, r in zip(para, rating):
        print(r.text + " - " + p.text)                      # printing the comments and rating of the user
        if r.text == '5':                                   # five ratings
            five = five + 1
        elif r.text == '4':                                   # four ratings
            four = four + 1
        elif r.text == '3':                                   # three ratings
            three = three + 1
        elif r.text == '2':                                   # two ratings
            two = two + 1
        elif r.text == '1':                                   # one ratings
            one = one + 1
        else:
            count = count+1

# count of different ratings

print("Five ratings : ",five)
print("Four ratings : ",four)
print("Three ratings : ",three)
print("Two ratings : ",two)
print("One ratings : ",one)