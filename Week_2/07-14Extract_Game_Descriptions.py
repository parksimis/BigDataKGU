# Practice 1 : extract game descriptions
# 구글 플레이스토어에서 게임 설명을 크롤링하기

from selenium import webdriver
from bs4 import BeautifulSoup

driver_path = '../resources/chromedriver'  # driver path
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
    div_descr.append(description)


browser.quit()


from konlpy.tag import Okt
import pytagcloud
from collections import Counter

okt = Okt()
for sentence in div_descr:
    nouns = okt.nouns(sentence)
    count = Counter(nouns)


import pytagcloud
tag = count.most_common(100)
tag_list = pytagcloud.make_tags(tag, maxsize=50)
pytagcloud.create_tag_image(tag_list, 'word_cloud.jpg', size=(900, 600), fontname='Korean', rectangular=False)

import webbrowser
webbrowser.open('word_cloud.jpg')