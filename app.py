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

    text= event.message.text
    # text = u +text
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
        message9 = TextSendMessage(text='今天也辛苦了呢！')
        _message9 = TextSendMessage(text='讓告解少女為您分擔吧！')
        line_bot_api.reply_message(event.reply_token, [message9,_message9])
    elif 0.5 > s1 and s1 >= 0.45:
        message10 = TextSendMessage(text='請問發生什麼了嗎？')
        line_bot_api.reply_message(event.reply_token, message10)
    elif 0.55 > s1 and s1 >= 0.5:
        message10 = TextSendMessage(text='今天過得怎麼樣呢？')
        _message10 = TextSendMessage(text='一切都還順利嗎？')
        line_bot_api.reply_message(event.reply_token, [message10,_message10])    
    elif s1 >= 0.55:
        s1 = TextSendMessage(text = s1.sentiments)    
        line_bot_api.reply_message(event.reply_token, s1)
            
import os

if __name__ == "__main__":
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    
