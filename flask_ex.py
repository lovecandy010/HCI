import os
import dialogflow_v2 as dialogflow
from flask import Flask, redirect, url_for, request, render_template
from selenium import webdriver

#원래 flask
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '_________' # json인증서 명
def detect_intent_texts(project_id, session_id, texts, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    for text in texts:
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result.fulfillment_text
    
def detect_intent_name(project_id, session_id, texts, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    for text in texts:
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result.intent.display_name

#웹크롤링용 추가
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver=webdriver.Chrome('C:/Users/khs/Desktop/templated-theory/chromedriver.exe',chrome_options=options)

#요기에 있던거를 밑으로 내림

#요기부터가 html과 연동
app = Flask(__name__) # Flask 객체를 생성하고 그 이름을 app 으로 설정
project_id = "sample1-bmhcdx"
session_id = "12124fejkffjksl"

@app.route('/',methods=['GET', 'POST']) # route 설정, URL 을 설정하는 것이다.
@app.route('/index',methods=['GET', 'POST'])
def page_main():    
    return render_template('index.html')

@app.route('/google_map2.html',methods=['GET', 'POST'])
def page_change():
    return render_template('google_map2.html')

@app.route('/medibot/<msg>', methods=['GET', 'POST'])
def medibot_dialogflow(msg):  
    ans = detect_intent_texts(project_id, session_id, [msg], 'en')
    intent_name=detect_intent_name(project_id, session_id, [msg], 'en')
    #요기부터 추가된부분
    if msg=='google_map2.html':
        return render_template('google_map2.html')
    
    if intent_name=='메뉴 추천' :
        return render_template('index.html',ans=ans)
    elif intent_name=='음식점 찾기' :
        #요기부터 크롤링하기위해 따온부분
        a=ans.split("'",4)             #여기서 대답을 5개로 자름. 2번째와 4번째에 메인이 들어감
        search_x=a[1]
        search_y=a[3]
        search_msg = search_x +"%20"+ search_y
        '''
        base_url='https://www.mangoplate.com/search/'
        search_what=(search_msg)
        url = base_url+search_what
        driver.get(url)
        '''
        
        #직접검색 추가하기
        base_url='https://www.mangoplate.com/search/'
        url=base_url+search_msg
        driver.get(url)
        
        #driver.switch_to_frame('fb_xdm_frame_https')       #웹페이지 시작할때 광고뜰때를 대비
        
        #elem=driver.find_element_by_name("main-search")
        
        #elem.clear()
        
        #elem.send_keys(search_msg)
        
        #frame_switch("#fb_xdm_frame_https")
        
        #btn_click = driver.find_element_by_class_name("btn-search")
        
        #btn_click.click()
        #요기까지가 직접검색 추가된내용
        
        body = driver.find_element_by_tag_name('body')
        
        datalist = body.find_elements_by_class_name('info')
        
        imgs=driver.find_elements_by_css_selector('img.center-croping.lazy')
        
        #이미지 크롤링용
        j=0           #이미지용 그냥변수
        textI="\n"    #이미지 저장용 (전체 다 저장됨)
        I=[]          #이미지 분할해서 저장용
        for img in imgs:
            if j>3:                  #이미지 4개 저장(0,1,2,3)
                break
            else:
                if 'http' in img.get_attribute('src'):
                    textI=img.get_attribute('src')           #이미지 url 추출
                    I.append(textI)                          #그걸 I(j)에 넣음
                    I[j]=textI
                    print('I[',j,']는',I[j],"\n")
                    j+=1
        
        
        #원래 text 크롤링용
        k=0
        textT="\n"
        T=[]          #텍스트 분할해서 저장용
        for data in datalist:
            if k>3:                     #텍스트 4개 저장(0,1,2,3)
                break
            else:
                textT=data.text         #텍스트 추출
                #textT += texty
                T.append(textT)
                print("T[",k,"]는",T[k],"\n")
                k+=1
        
        #요기까지가 크롤링용 추가된 내용
    
        #요기까지 추가된부분
        
        #요기서부터는 원래 부분
        
        if k==0:
            ans="미안 주변에 맛집이 없네"
            return render_template('index.html', ans=ans)
        
        elif k==1:
            info_0 = T[0]
            img_0 = I[0]
            return render_template('index.html', ans=ans,info_0=info_0,img_0=img_0)
        
        elif k==2:
            info_0 = T[0]
            info_1 = T[1]            
            img_0 = I[0]
            img_1 = I[1]            
            return render_template('index.html', ans=ans,info_0=info_0,img_0=img_0,info_1=info_1,img_1=img_1)
        
        elif k==3:
            info_0 = T[0]
            info_1 = T[1]
            info_2 = T[2]
            img_0 = I[0]
            img_1 = I[1]
            img_2 = I[2]            
            return render_template('index.html', ans=ans,info_0=info_0,img_0=img_0,info_1=info_1,img_1=img_1,info_2=info_2,img_2=img_2)
        
        else:
            info_0 = T[0]
            info_1 = T[1]
            info_2 = T[2]
            info_3 = T[3]
            img_0 = I[0]
            img_1 = I[1]
            img_2 = I[2]
            img_3 = I[3]
            return render_template('index.html',ans=ans,info_0=info_0,info_1=info_1,info_2=info_2,info_3=info_3,img_0=img_0,img_1=img_1,img_2=img_2,img_3=img_3)
        
    else:
        return render_template('index.html',ans=ans)
    
@app.route('/action',methods = ['POST', 'GET'])
def action():
    if request.method == 'POST':
        msg = request.form['msg']
        return redirect(url_for('medibot_dialogflow', msg=msg))
    else:
        msg = request.args.get('msg')
        return redirect(url_for('medibot_dialogflow', msg=msg))

if __name__ == '__main__':
    app.run(debug=True) # app.run(host=’0,0,0,0’)으로 설정하면 외부에서 접근 가능