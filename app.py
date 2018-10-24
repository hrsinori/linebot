from flask import Flask, request, abort
import os
import sys
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

ACCESS_TOKEN= os.environ['ACCESS_TOKEN']
SECRET= os.environ['CHANNEL_SECRET']

# Channel Access Token
line_bot_api = LineBotApi(ACCESS_TOKEN)
# Channel Secret
handler = WebhookHandler(SECRET)


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
    message = TextSendMessage(text='您好，請問今天有什麼事要訴說呢？')
    line_bot_api.reply_message(event.reply_token, message)

string MyLineChannelAccessToken = "隱藏起來";
/// <summary>
/// </summary>
/// <returns></returns>
[HttpPost]
[Route("api/LineBotApi/post")]
public async void Post()
{
    try
    {
        string postData = Request.Content.ReadAsStringAsync().Result;
        var ReceivedMessage = isRock.LineBot.Utility.Parsing(postData);
        var bot = new isRock.LineBot.Bot(this.MyLineChannelAccessToken);
        string userCommandString = ReceivedMessage.events[0].message.text;
        LineBotMember _service = new LineBotMember();
        string message = string.Empty;

        if (userCommandString == "save")
        {
            _service.InsertID(ReceivedMessage.events[0].source.userId);
            var call = Task.Run(() =>
            {
                bot.ReplyMessage(ReceivedMessage.events[0].replyToken,
                    string.Format("紀錄成功: {0}", ReceivedMessage.events[0].source.userId));
            });
        }
     }
      catch (Exception ex)
      {
                string postData = Request.Content.ReadAsStringAsync().Result;
                var ReceivedMessage = isRock.LineBot.Utility.Parsing(postData);
                var bot = new isRock.LineBot.Bot(this.MyLineChannelAccessToken);
                var call = Task.Run(() =>
                {
                    bot.ReplyMessage(ReceivedMessage.events[0].replyToken,
                        string.Format("錯誤資訊:{0}", ex.Message));
                });
       }
}
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
