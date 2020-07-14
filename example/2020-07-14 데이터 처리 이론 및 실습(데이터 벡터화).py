# Image embedding example
## Load image
## Represent as vector(grey, RGB)

from skimage import data, io
from matplotlib import pyplot as plt


camera = data.camera() # camera image ; grey scale

io.imshow(camera)
plt.show()

print(type(camera), camera.shape)
print(camera)

cat = data.chelsea() # cat is a 300-by-451 pixel image with three channels (red, green, and blue)

io.imshow(cat)
plt.show()

print(type(cat), cat.shape)
print(cat)

# Task 6  image color detection

import numpy as np
import cv2 as cv
from skimage import io
import matplotlib.pyplot as plt


red = np.array([[0, 80, 80], [10, 255, 255]])
orange = np.array([[13, 80, 80], [23, 255, 255]])
yellow = np.array([[25, 80, 80], [35, 255, 255]])
green = np.array([[40, 80, 80], [80, 255, 255]])
blue = np.array([[80, 80, 80], [140, 255, 255]])
pink = np.array([[145, 80, 80], [160, 255, 255]])
red_high = np.array([[170, 80, 80], [180, 255, 255]])

color_names = ["red", "orange", "yellow", "green", "blue", "pink"]
colors = [red, orange, yellow, green, blue, pink, red_high]

url = "https://lh3.googleusercontent.com/0ov1-rv3uTpw4KQphQUemyHPslZ4a8q-5C3c89lbXUKjbo9RzVaYH4F8_sMJBm4dsR0"
#url = "https://lh6.ggpht.com/hIY78puIGVb26VFsWexvVe5T00nfLK9IKbg8uHKK9MwyAO0aPySjopPh1NUSMJYM2UWX"

image = io.imread(url) # Load image from url
image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV) # Converts images from BGR to HSV

ratios_dic = {}
for i in range(len(colors)):
    mask = cv.inRange(hsv, colors[i][0], colors[i][1])
    io.imshow(mask)
    plt.show()

    if i != len(colors) - 1:
        ratios_dic[color_names[i]] = np.count_nonzero(mask) / float(np.prod(mask.shape)) * 100
    else:
        ratios_dic[color_names[0]] = ratios_dic[color_names[0]] + np.count_nonzero(mask) / float(np.prod(mask.shape)) * 100

print(ratios_dic)

# 텍스트 데이터 embedding

## - 텍스트 데이터 분석
## * 단어 수준으로 문서 쪼개기 - tokenization
## * 단어를 일반형으로 변환 - stemming
## * 불필요한 단어 제거 - stopwords
## * 동의어 처리

import pytagcloud



tag = [('hello', 100), ('world', 80), ('nice', 60), ('to', 20), ('meet', 10), ('Park', 200),
       ('Hi', 400), ('Bye', 300)]
tag_list = pytagcloud.make_tags(tag, maxsize=50)
pytagcloud.create_tag_image(tag_list, 'word_cloud.jpg', size=(300, 600), rectangular=False)

import webbrowser
webbrowser.open('word_cloud.jpg')