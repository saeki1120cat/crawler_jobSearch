from __future__ import unicode_literals
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TemplateSendMessage,
    ButtonsTemplate,
    PostbackEvent,
    PostbackTemplateAction,
    FlexSendMessage
)

import configparser

import crawler_jobSearch as cj
import flex_template as ft

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
parser = WebhookParser(config.get('line-bot', 'channel_secret'))


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        events = parser.parse(body, signature)

    except InvalidSignatureError:
        abort(400)
        return 'OK'

    for event in events:
        if isinstance(event, MessageEvent):
            if event.message.text == "找工作":
                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TemplateSendMessage(
                        alt_text='Buttons template',
                        template=ButtonsTemplate(
                            title='Web',
                            text='請選擇網站',
                            actions=[
                                PostbackTemplateAction(
                                    label='104',
                                    text='104',
                                    data='A&104'
                                ),
                                PostbackTemplateAction(
                                    label='1111',
                                    text='1111',
                                    data='A&1111'
                                ),
                                PostbackTemplateAction(
                                    label='cakeresume',
                                    text='cakeresume',
                                    data='A&cakeresume'
                                )
                            ]
                        )
                    )
                )
        elif isinstance(event, PostbackEvent):  # 如果有回傳值事件

            if event.postback.data[0:1] == "A":

                area = event.postback.data[2:]

                line_bot_api.reply_message(
                    event.reply_token,
                    TemplateSendMessage(
                        alt_text='Buttons template',
                        template=ButtonsTemplate(
                            title='keywords',
                            text='請選擇關鍵字',
                            actions=[
                                PostbackTemplateAction(  # 將第一步驟選擇的網站，包含在第二步驟的資料中
                                    label='python',
                                    text='python',
                                    data='B&' + area + '&python'
                                ),
                                PostbackTemplateAction(
                                    label='sql',
                                    text='sql',
                                    data='B&' + area + '&sql'
                                ),
                                PostbackTemplateAction(
                                    label='日本',
                                    text='日本',
                                    data='B&' + area + '&日本'
                                )
                            ]
                        )
                    )
                )

            elif event.postback.data[0:1] == "B":

                result = event.postback.data[2:].split('&')  # 回傳值的字串切割
                web = result[0]
                keyword_str = result[1]
                cj.main(web, keyword_str)
                cj.crawler_jobSearch(web)

                ft.flex_template(cj.df)

                messages = FlexSendMessage(alt_text="找工作的訊息",contents = ft.msg)

                line_bot_api.reply_message(event.reply_token, messages)


if __name__ == "__main__":
    app.run()