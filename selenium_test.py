# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:22:42 2019

@author: khs
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver=webdriver.Chrome('C:/Users/khs/Desktop/templated-theory/chromedriver.exe',chrome_options=options)

base_url='https://www.mangoplate.com/search/'
search_what=("흑석동"+"%20"+"짜장")
url = base_url+search_what
driver.get(url)

body = driver.find_element_by_tag_name('body')

datalist = body.find_elements_by_class_name('list-restaurant-item')

i=0
textI=""

for data in datalist:
    if i>5:
        break
    else:
        texty=data.text
        i+=1
        textI += texty
        print(texty,"\n",i)

'''
for data in datalist:
    while i<5:
        texty=data.text
        i+=1
        textI += texty
        print(textI,"\n",i)
'''
     

'''
for data in datalist:
    texty = data.text
    print(texty,"\n")
'''

print("왜안나오지","\n",textI,"\n")
'''
elem = driver.find_element_by_name("main-search")
elem.clear()
elem.send_keys("인사동"+" "+"치킨")
elem.submit()
'''
input("Any Key for Text")
driver.close()