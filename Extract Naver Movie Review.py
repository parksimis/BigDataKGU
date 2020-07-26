from selenium import webdriver
from bs4 import BeautifulSoup

# 네이버에서 평점순(모든영화) 랭킹 50위까지의 영화의 평점, 리뷰, 날짜를 가져오기
# 각 영화의 한 페이지당 10개씩, 총 20페이지의 영화 리뷰, 도합 영화당 200개씩의 영화리뷰

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

    # 각 영화의 평점 사이트로 바로 접속하게 하는 코드
    movie_url = movie_link.a['href']  # 각 영화의 사이트를 가져옴
    movie_url= movie_url.split('basic') # 각 영화의 사이트를 basic을 기준으로 분리
    movie_url = "point".join(movie_url) # 분리된 사이트를 point를 넣어 합침

    # 합쳐진 사이트로 들어감
    browser.get('https://movie.naver.com/' + movie_url)
    movie_name = browser.find_element_by_css_selector(".mv_info_area .h_movie a:nth-child(1)").text
    time.sleep(1)

    # 각 영화의 리뷰 페이지의 첫 링크를 가져옴
    review_link = browser.find_element_by_css_selector('.ifr_module2 iframe').get_attribute('src')
    time.sleep(1)

    # 각 영화의 20페이지까지 가져옴
    for i in range(1, 21):
        new_url = review_link + "&page=" + str(i)
        browser.get(new_url)

        # 영화가 담겨있는 box 가져옴
        boxes = browser.find_elements_by_css_selector('.score_result li')

        for j in range(len(boxes)):
            score = boxes[j].find_element_by_css_selector('.star_score').text
            ment = boxes[j].find_element_by_css_selector('#_filtered_ment_'+str(j)).text
            date = boxes[j].find_element_by_css_selector('.score_reple dt em:nth-child(2)').text
            naver_reviews.append([movie_name, score, ment, date])

browser.quit()

# csv 파일로 변환

import numpy as np
import pandas as pd

columns = ["영화제목", "평점", "리뷰", "날짜"]
naver_reviews = np.array(naver_reviews)

naver_df = pd.DataFrame(naver_reviews, columns=columns)


display(naver_df.head())

naver_df.to_csv('naver movie review.csv')
