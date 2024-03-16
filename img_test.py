from selenium import webdriver

print("접속중")
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver=webdriver.Chrome('C:/Users/khs/Desktop/templated-theory/chromedriver.exe',chrome_options=options)

url='https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%ED%81%B4%EB%A0%88%EB%93%9C'
driver.get(url)

imgs=driver.find_elements_by_css_selector('img._img')

i=0
textP=""
a=[]

for img in imgs:
    if i>3:
        break
    else:
        if 'http' in img.get_attribute('src'):
            textP=img.get_attribute('src')
            a.append(textP)
            print(img.get_attribute('src'),"\n")
            print('P는',textP,"\n")
            print("a[",i,"]는",a[i],"\n")
            i+=1