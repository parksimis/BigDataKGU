from selenium import webdriver
from bs4 import BeautifulSoup

# 네이버에서 평점순(모든영화) 랭킹 50위까지의 영화의 평점, 리뷰를 가져오기

driver_path = 'resources/chromedriver'
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200721'

'''browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')

# 첫 화면에서 50위까지의 영화 상세정보 사이트를 가져옴
ranking_links = soup.find_all('div', {"class" : "tit5"}, {'a' : 'href'})
import time
# time.sleep(1)

for movie_link in ranking_links:
    movie_url = movie_link.a['href']
    browser.get('https://movie.naver.com/' + movie_url)
    button = browser.find_element_by_css_selector('.end_sub_tab li:nth-child(5) a').click()
    new_url = browser.page_source
    soup = BeautifulSoup(new_url, 'html.parser')'''


driver_path = 'resources/chromedriver'
url = 'https://movie.naver.com/movie/bi/mi/point.nhn?code=171539'

browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver
browser.get(url)
temp_link = browser.page_source
soup = BeautifulSoup(temp_link, 'html.parser')
temp = soup.find_all({'class' : "ifr_area basic_ifr"}, {'class' : 'score_result'})
#temp = browser.find_elements_by_css_selector('.ifr_area.basic_ifr .score_result .score_reple')

browser.quit()

