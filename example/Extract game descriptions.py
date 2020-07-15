# Practice 1 : extract game descriptions
# 구글 플레이스토어에서 게임 설명을 크롤링하기

from selenium import webdriver
from bs4 import BeautifulSoup

driver_path = '../resources/chromedriver' # driver path
url = 'https://play.google.com/store/apps/top/category/GAME'

browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver
browser.get(url)

button = browser.find_element_by_css_selector('.W9yFB a').click()
page = browser.page_source
soup = BeautifulSoup(page, 'html.parser')
links = soup.find_all('div', {'class' : 'b8cIId ReQCgd Q9MA7b'})



div_descr = []
for link in links:
    new_url = link.a['href']
    browser.get("https://play.google.com"+new_url)
    description = browser.find_element_by_css_selector('.DWPxHb div:nth-child(1)').text
    div_descr.append( description)


browser.quit()


'''import pytagcloud

tag = [('hello', 100), ('world', 80), ('nice', 60), ('to', 20), ('meet', 10), ('Park', 200),
       ('Hi', 400), ('Bye', 300)]
tag_list = pytagcloud.make_tags(tag, maxsize=50)
pytagcloud.create_tag_image(tag_list, 'word_cloud.jpg', size=(300, 600), rectangular=False)

import webbrowser
webbrowser.open('word_cloud.jpg')'''