from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver=webdriver.Chrome('C:/Users/khs/Desktop/templated-theory/chromedriver.exe',chrome_options=options)
'''
def frame_switch(css_selector):
  driver.switch_to.frame(driver.find_element_by_css_selector(css_selector))
'''
url='https://www.mangoplate.com/'
driver.get(url)

#driver.switch_to_frame('fb_xdm_frame_https')       #웹페이지 시작할때 광고뜰때를 대

elem=driver.find_element_by_name("main-search")

elem.clear()

elem.send_keys("흑석동 짜장")

#frame_switch("#fb_xdm_frame_https")

btn_click = driver.find_element_by_class_name("btn-search")

btn_click.click()

body = driver.find_element_by_tag_name('body')

datalist = body.find_elements_by_class_name('info')

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