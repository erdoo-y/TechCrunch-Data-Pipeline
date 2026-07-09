import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import csv
import time
url= 'https://techcrunch.com/feed/'
data= urllib.request.urlopen(url).read()
tree= ET.fromstring(data)
page_name= tree.find('channel/title')
print(page_name.text)
#defining the xmlns for 'dc' so it doesn't blow up when 'dc:creator' is called
namespace={'dc':"http://purl.org/dc/elements/1.1/"}
with open('Latest_TechCrunchNews.csv','w', newline='',encoding='utf-8-sig') as file:
    writer=csv.writer(file)
    writer.writerow(['Headline', 'Link', 'Date Published', 'Category', 'Author'])
    for tag in tree.findall('channel/item'):
        title= tag.find('title').text
        link= tag.find('link').text
        date_published= tag.find('pubDate').text.replace('+0000','') #removes the ugly timezone
        category= tag.findall('category')
        # loops through category and gets a list then joins them together by','and''
        cat=', '.join([cat.text for cat in category])
        author= tag.find('dc:creator',namespace).text

        writer.writerow([title, link, date_published, cat, author])
        time.sleep(2) #polite 2 seconds break in between
print ('All done!')
