# Python으로 웹페이지의 HTML 소스 받기

import requests

raw = requests.get("http://147.46.178.16:33333/table.html",
headers={'User-Agent': 'Mozilla/5.0'})

#print(raw.text)

# BeatifulSoup를 사용해서 소스 분석

from bs4 import BeautifulSoup
html = BeautifulSoup(raw.content, "html.parser", from_encoding="utf-8")
#print(html)

test = html.select_one('tr th')
# Soup 변수에서는 추후 selector를 사용하여 원하는 정보를 빼오는 것이 가능하다.
print(test)
print(test.text)
print(test.get('class'))

selectfunction = html.select('tr th')
print("selectfunction : \n", selectfunction)
print('text만 나오게하려면 :', selectfunction[0].text)
for d in selectfunction:
    print(d.text)


# Practice
## 산기대 홈페이지에서 한글 학과명의 태그를 전부 가져오기

raw = requests.get("http://www.kpu.ac.kr/contents/main/cor/kcollege.html",
headers={'User-Agent': 'Mozilla/5.0'})

html = BeautifulSoup(raw.content, "html.parser", from_encoding="utf-8")

body = html.select(".label.ko")

for dept in body:
    print(dept.text)


# Selenium을 활용해 동적 script 크롤링

from selenium import webdriver

driver_path = '../resources/chromedriver' #driver path
url = "http://147.46.178.16:33333/javascript.html"

browser = webdriver.Chrome(executable_path=driver_path)
browser.get(url)


browser.find_element_by_css_selector('body a').click()
import time
time.sleep(1)
print(browser.page_source)
browser.quit()

# Practice Selenium을 통해 네이버 블로그 크롤링
import time

driver_path = '../resources/chromedriver' #driver path
browser = webdriver.Chrome(executable_path=driver_path)

browser.get("https://blog.naver.com")

time.sleep(1)

boxes = browser.find_elements_by_css_selector('div.info_post')
print(len(boxes))

for i in range(len(boxes)):
    try:
        title = boxes[i].find_element_by_css_selector('a strong').text
        author = boxes[i].find_element_by_css_selector('.name_author').text
        replies = boxes[i].find_element_by_css_selector(".reply em").text
        thumbnailurl = boxes[i].find_element_by_css_selector('img').get_attribute('bg-image')
        print(replies + '\t' + author + '\t' + title + '\t' + thumbnailurl)

    except:
        print("There is an error with " +str(i+1) +" 번째")

browser.quit()


# Practice
## 산업일보 홈페이지에서 코로나를 검색해보기

driver_path = '../resources/chromedriver' #driver path
browser = webdriver.Chrome(executable_path=driver_path)

browser.get("http://kidd.co.kr/")
time.sleep(1)

textarea = browser.find_element_by_css_selector("#form_find")
textarea.send_keys('코로나')
button = browser.find_element_by_css_selector('#sch_form input:nth-child(3)').click()
