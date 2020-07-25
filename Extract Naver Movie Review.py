from selenium import webdriver
from bs4 import BeautifulSoup

# 네이버에서 평점순(모든영화) 랭킹 50위까지의 영화의 평점, 리뷰를 가져오기

driver_path = 'resources/chromedriver'
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200721'

browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')

# 첫 화면에서 50위까지의 영화 상세정보 사이트를 가져옴
ranking_links = soup.find_all('div', {"class" : "tit5"}, {'a' : 'href'})

import time

naver_reviews = []

for movie_link in ranking_links:
    movie_url = movie_link.a['href']
    browser.get('https://movie.naver.com/' + movie_url)
    new_url = browser.page_source
    soup = BeautifulSoup(new_url, 'html.parser')
    #button = browser.find_element_by_css_selector('.end_sub_tab li:nth-last-child(3) a').click()
    button = browser.find_element_by_css_selector('.end_sub_tab li').get_attribute('title').click()
    #button[title='평점'].a['href'].click()
    time.sleep(1)
    # new_url = browser.page_source
    # soup = BeautifulSoup(new_url, 'html.parser')

    # 각 영화의 리뷰 페이지의 첫 링크를 가져옴
    review_link = browser.find_element_by_css_selector('.ifr_module2 iframe').get_attribute('src')
    browser.get(review_link) # 링크 접속
    time.sleep(1)
    # 각 영화의 20페이지까지 가져옴
    for i in range(1, 3):
        new_url = review_link + "&page=" + str(i)
        browser.get(new_url)

        # 영화가 담겨있는 box 가져옴
        boxes = browser.find_elements_by_css_selector('.score_result li')

        for i in range(len(boxes)):
            a = boxes[i].find_element_by_css_selector('.star_score').text
            b = boxes[i].find_element_by_css_selector('#_filtered_ment_'+str(i)).text
            c = boxes[i].find_element_by_css_selector('.score_reple dt em:nth-child(2)').text
            naver_reviews.append([a, b, c])
            #print(boxes[i].find_element_by_css_selector('.star_score').text)
            #print(boxes[i].find_element_by_css_selector('#_filtered_ment_'+str(i)).text)
            #print(boxes[i].find_element_by_css_selector('.score_reple dt em:nth-child(2)').text)

browser.quit()

