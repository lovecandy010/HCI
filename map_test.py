from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver=webdriver.Chrome('C:/Users/khs/Desktop/templated-theory/chromedriver.exe',chrome_options=options)


url = 'https://www.google.com/maps/place/%EC%84%B1%EB%AF%BC%EC%96%91%EA%BC%AC%EC%B9%98/@37.5075037,126.9625364,18z/data=!3m1!4b1!4m5!3m4!1s0x357ca1e7f2efb571:0x5b8d07f3a3de0d4a!8m2!3d37.5075037!4d126.9636307?hl=ko'
driver.get(url)

def crawl(url):
    data=requests.get(url)
    print(data,url)
    return data.content

print(crawl(url))

  
        
#print("왜안나오지","\n",text,"\n", "이거에 나와야됨")
'''
elem = driver.find_element_by_name("main-search")
elem.clear()
elem.send_keys("인사동"+" "+"치킨")
elem.submit()
'''
input("Any Key for Text")
driver.close()