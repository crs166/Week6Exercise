#Imports requests and Scrapy
import scrapy
import requests
from scrapy import Selector

#requests website
r = requests.get("https://www.xml-sitemaps.com/download/www.isolezwe.co.za-7447b2b3b/sitemap.xml?view=1")

#selector for selecting page elements
sel = Selector(text = r.text)



arr = (sel.css("loc::text").getall())

print(arr)

httpsArr = []
x = 0

for i in arr:
    if(i[0:4] == 'http'):
        httpsArr.append(i)
for i in httpsArr:
    r1 = requests.get(i)
    sel = Selector(text = r1.text)
    print(sel.xpath("/[@class='articleBodyMore//p/text()']"))
