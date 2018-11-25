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
    s1 = TextSendMessage(text = s1.sentiments)
    line_bot_api.reply_message(event.reply_token, s1)
            
import os

if __name__ == "__main__":
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    
