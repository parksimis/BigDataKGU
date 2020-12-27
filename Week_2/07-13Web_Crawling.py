
from selenium import webdriver

# Task 1 : open an URL

'''
print("Task 1 : open an URL")
driver_path = '../resources/chromedriver' #driver path
url = 'https://play.google.com/store/apps/top/category/GAME'

browser = webdriver.Chrome(executable_path=driver_path) #Chrome driver
browser.get(url)

browser.quit()


urls = [

"https://play.google.com/store/apps/category/GAME_EDUCATIONAL", # categories
"https://play.google.com/store/apps/category/GAME_WORD",

]

# Task 2 : open multiple URLs
print("Task 2 : open multiple URLs")
browser = webdriver.Chrome(executable_path=driver_path)

for url in urls:
    browser.get(url)
    

browser.quit()

'''

# Task 3 : beautiful soup test
## Represents the documents as a nested data structure
print("Task 3 : beautiful soup test")
from bs4 import BeautifulSoup

html_doc= """
<html><head><title> The Dormouse's story </title></head>
<body>
<p class="title"><b> The Dormouse's story</b></p>
<p class="story"> Once upon a time there were tree little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>


soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
"""
# Task 3-1 : navigate structures
'''print("Task 3-1 : negvigate structures")
tag = soup.a # soup에서 제일 처음 등장하는 a 태그 전체를 가져옴
print(tag)
print(tag.names)
print(tag.attrs) # 해당 태그의 모든 attribute를 dictionary 형태로 가져옴
print(tag.string) # tag 안에 있는 string(content)을 가져옴
print(tag['class']) # class attribute 안에 있는 값

print(soup.title) # title 태그를 가져옴
print(soup.title.name) # title의 이름을 가져옴
print(soup.title.string) # 안에 적힌 string

print(soup.title.parent.name) # parent - head
print(soup.title.parent.title.string)
print(soup.head.contents[0].string) # contents : children as a list

print(soup.p) # p 태그가 가장 먼저 출현하는 것을 가져옴
print(soup.p['class'])
print(soup.a)
print(soup.find_all('a')) # a 태그인 것을 다 가져옴
print(soup.find(id='link3')) # id가 Link3인 tag를 가져옴
print(soup.find(id='link3').string)

for link in soup.find_all('a'):
    print(link.get('href'))
    print(link['href'])

print(soup.get_text())'''


# Task 4 : parse top game charts
## Open a top game charts page
## Parse and represent as HTML tree

from selenium import webdriver
from bs4 import BeautifulSoup
'''
driver_path = '../resources/chromedriver'
url = 'https://play.google.com/store/apps/top/category/GAME'

browser = webdriver.Chrome(executable_path=driver_path) # Chrome Driver
browser.get(url)
page = browser.page_source
browser.quit()

soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())
'''


# Task 5 : extract links to game ranks
from selenium import webdriver
from bs4 import BeautifulSoup

'''driver_path = '../resources/chromedriver' # driver path
url = 'https://play.google.com/store/apps/top/category/GAME'

browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver
browser.get(url)
page = browser.page_source

soup = BeautifulSoup(page, "html.parser")
links = soup.find_all('div', {'class': 'W9yFB'}) # find all links to rankings

print(links)

for link in links:
    new_url = link.a['href']
    browser.get("https://play.google.com"+new_url)
browser.quit()'''

# Practice 1 : extract game descriptions
# 구글 플레이스토어에서 게임 설명을 크롤링하기

driver_path = '../resources/chromedriver'  # driver path
url = 'https://play.google.com/store/apps/top/category/GAME'

browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver
browser.get(url)
page = browser.page_source

soup = BeautifulSoup(page, "html.parser")
links = soup.find_all('div', {'class': 'b8cIId ReQCgd Q9MA7b'})
#boxes = browser.find_elements_by_css_selector(".b8cIId.ReQCgd.Q9MA7b a").text

'''import time

for link in boxes:
    browser.get(link)
    time.sleep(1)'''


div_descr = []
for link in links:
    new_url = link.a['href']
    browser.get("https://play.google.com"+new_url)
    new_page = browser.page_source
    soup = BeautifulSoup(new_page, "html.parser")
    new_link = soup.find_all('div', {'class' : 'W4P4ne'})[0].text
    div_descr.append(new_link)

print("Description: ", new_link)
browser.quit()
