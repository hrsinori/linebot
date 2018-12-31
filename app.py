from flask import Flask, request, abort

import urllib.request, json
import requests
from bs4 import BeautifulSoup

import os
import sys
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from snownlp import SnowNLP
from snownlp import seg

import sys
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

app = Flask(__name__)

ACCESS_TOKEN= os.environ['ACCESS_TOKEN']
SECRET= os.environ['CHANNEL_SECRET']

# Channel Access Token
line_bot_api = LineBotApi(ACCESS_TOKEN)
# Channel Secret
handler = WebhookHandler(SECRET)

pm_site = {}

@app.route("/")
def hello_world():
    return "hello world!"


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
  
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
#     _message = TextSendMessage(text='Nice to meet you!')
#     _message = TextSendMessage(text=(event.source.user_id)) #reply userid
#     line_bot_api.reply_message(event.reply_token, _message)  
    # message = TextSendMessage(text=event)
#     print(event)    
    text = event.message.text
    s = SnowNLP(text)
    s1 = SnowNLP(s.sentences[0])
    s1 = s1.sentiments
    '''            
    s = SnowNLP(text)
    s1 = SnowNLP(s.sentences[0])
    s1.sentiments 
    s1 = TextSendMessage(text = s1.sentiments)    
    line_bot_api.reply_message(event.reply_token, s1)
    ''' 
    if text == '謝謝' or text == '謝謝你' or text == '幹' or text == '去你的' or text == '開心' or text == '悲傷' or text == '對阿' or text == '對啊' :
           pass   
    elif text == '好的' or text == '知道了' or text == '好喔' :
            message00 = TextSendMessage(text='看來您能理解呢，真是太好了！')
            _message00 = TextSendMessage(text='請繼續加油吧！')
            message00_ = ImageSendMessage(
            original_content_url='https://i.imgur.com/TIB3QUp.jpg',
            preview_image_url='https://i.imgur.com/TIB3QUp.jpg'
            )
            line_bot_api.reply_message(event.reply_token, [message00,_message00,message00_])    
    elif text == '你好' or text == '妳好' or text == '哈囉' or text == 'hello' or text == 'Hello' or text == '嗨' :
            message01 = TextSendMessage(text='您好，請問今天有什麼事想和告解少女說的嗎？')
            message01_ = ImageSendMessage(
            original_content_url='https://i.imgur.com/xfPwnn8.jpg',
            preview_image_url='https://i.imgur.com/xfPwnn8.jpg'
            )
            line_bot_api.reply_message(event.reply_token, [message01,message01_])    
    elif text == '跟你說喔' or text == '我跟你說' :
            message02 = TextSendMessage(text='請問怎麼了嗎？')
            line_bot_api.reply_message(event.reply_token, message02)    
        # text = u +text
    else :  
            s = SnowNLP(text)
            s1 = SnowNLP(s.sentences[0])
            s1 = s1.sentiments
            if 0.05 > s1 and s1 >= 0:
                _message1 = TextSendMessage(text='今天的您令人有些擔心呢。')
                message1 = TextSendMessage(text='請問您需要幫助，或是找人聊聊嗎？')
                message1_ = TextSendMessage(text='告解少女隨時都在您身邊喔(*・∀-)')
                line_bot_api.reply_message(event.reply_token,[_message1, message1, message1_])
            elif 0.1 > s1 and s1 >= 0.05:
                message2 = TextSendMessage(text='請問您還好嗎？')
                _message2 = TextSendMessage(text='任何事情都可以跟告解少女說喔(*’-^*)')
                line_bot_api.reply_message(event.reply_token, [message2,_message2])
            elif 0.15 > s1 and s1 >= 0.1:
                message3 = TextSendMessage(text='聽說透透氣對身心都很好呢。')
                _message3 = TextSendMessage(text='心情不好的時候就到外面走走吧(*･▽･*)')
                line_bot_api.reply_message(event.reply_token, [message3,_message3])
            elif 0.2 > s1 and s1 >= 0.15:
                message4 = TextSendMessage(text='今天發生什麼不愉快的事了嗎？')
                _message4 = TextSendMessage(text='這時候就好好放鬆一下自己吧(*ˊ∀ˋ*)')
                line_bot_api.reply_message(event.reply_token, [message4,_message4])    
            elif 0.25 > s1 and s1 >= 0.2:
                message5 = TextSendMessage(text='怎麼了嗎？')
                _message5 = TextSendMessage(text='不妨跟告解少女說說吧(´▽ˋ)')
                line_bot_api.reply_message(event.reply_token, [message5,_message5])
            elif 0.3 > s1 and s1 >= 0.25:
                message6 = TextSendMessage(text='今天很累了吧？')
                _message6 = TextSendMessage(text='但是別灰心，告解少女會陪您一起度過所有煩惱的！')
                line_bot_api.reply_message(event.reply_token, [message6,_message6])
            elif 0.35 > s1 and s1 >= 0.3:
                message7 = TextSendMessage(text='今天看起來心情很糟呢0.0')
                _message7 = TextSendMessage(text='想不想來點音樂呢？')
                line_bot_api.reply_message(event.reply_token, [message7,_message7])
            elif 0.4 > s1 and s1 >= 0.35:
                message8 = TextSendMessage(text='笑一個吧(oﾟ▽ﾟ)o')
                _message8 = TextSendMessage(text='笑容是可以化解任何不愉快的喔！')
                line_bot_api.reply_message(event.reply_token, [message8,_message8])
            elif 0.45 > s1 and s1 >= 0.4:
                message9 = TextSendMessage(text='事情總會好起來的，所以請您也打起精神吧！')
                line_bot_api.reply_message(event.reply_token, message9)
            elif 0.5 > s1 and s1 >= 0.45:
                message10 = TextSendMessage(text='今天也辛苦了呢！')
                _message10 = TextSendMessage(text='讓告解少女為您分擔吧！')
                line_bot_api.reply_message(event.reply_token, [message10,_message10])
            elif 0.55 > s1 and s1 >= 0.5:
                message10 = TextSendMessage(text='請問今天發生了什麼樣的事情呢？')
                line_bot_api.reply_message(event.reply_token, message10)
            elif 0.6 > s1 and s1 >= 0.55:
                message11 = TextSendMessage(text='今天也辛苦了！')
                _message11 = TextSendMessage(text='來和告解少女說說話吧～')
                line_bot_api.reply_message(event.reply_token, [message11,_message11])
            elif 0.65 > s1 and s1 >= 0.6:
                message12 = TextSendMessage(text='您看起來心情不錯呢(*ˊ∀ˋ*)')
                line_bot_api.reply_message(event.reply_token, message12)
            elif 0.7 > s1 and s1 >= 0.65:
                message13 = TextSendMessage(text='看起來是遇見了什麼美好的事物呢。')
                _message13 = TextSendMessage(text='希望能夠成為您生活的動力～')
                line_bot_api.reply_message(event.reply_token, [message13,_message13])
            elif 0.7 > s1 and s1 >= 0.65:
                message13 = TextSendMessage(text='看起來是遇見了什麼美好的事物呢。')
                _message13 = TextSendMessage(text='希望能夠成為您生活的動力～')
                line_bot_api.reply_message(event.reply_token, [message13,_message13])
            elif 0.75 > s1 and s1 >= 0.7:
                message13 = TextSendMessage(text='今天的您看起來心情很好呢！')
                _message13 = TextSendMessage(text='是不是發生什麼好事嘞呢？')
                line_bot_api.reply_message(event.reply_token, [message13,_message13])          
    if text != "":
        c=s1
        d=str(c)
        #GDriveJSON就輸入下載下來Json檔名稱
        #GSpreadSheet是google試算表名稱
        GDriveJSON = 'time.json'
        GSpreadSheet = 'time'
        while True:
            try:
                #scope = ['https://spreadsheets.google.com/feeds']
                scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
                key = SAC.from_json_keyfile_name(GDriveJSON, scope)
                gc = gspread.authorize(key)
                worksheet = gc.open(GSpreadSheet).sheet1
            except Exception as ex:
                print('無法連線Google試算表', ex)
                sys.exit(1)
            textt=""
            textt+= d
            if textt!="":
                worksheet.append_row((str(datetime.datetime.now()),textt))
                print('新增一列資料到試算表' ,GSpreadSheet)
                return textt 
        #開關	
        count=0
        #以下3個變數作為加總的時候用的 	
        number=0
        for i in values:
             if count==0:
                 count+=1
                 continue
        outputvalue = 'number{}'.format(number)
        return outputvalue 
        message20 = TextSendMessage(text=outputvalue)
        line_bot_api.reply_message(event.reply_token, [message20])    
 

import os

if __name__ == "__main__":
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    
