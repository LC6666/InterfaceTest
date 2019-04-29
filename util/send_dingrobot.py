# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

import json
from tests.runmethod import RunMethod

# https://oapi.dingtalk.com/robot/send?access_token=0adbaf26ecde631858af4ef70bd8550c814fa864c539e9eeede5b9c31f3f7173

class SendDingTalk:
    global url
    global headers
    url = 'https://oapi.dingtalk.com/robot/send?access_token=0adbaf26ecde631858af4ef70bd8550c814fa864c539e9eeede5b9c31f3f7173'
    headers = '{"Content-Type": "application/json ;charset=utf-8"}'

    # 发送text类型的消息
    # content 消息内容
    # atMobiles 被@人的手机号(在content里添加@人的手机号) list
    # isAtAll @所有人时：true，否则为：false
    def sendTextMsg(self,content,atMobiles=None,isAtAll=None):
        msg = {
        "msgtype": "text",
        "text": {
            "content": content
                },
        "at": {
            "atMobiles":
                atMobiles,
            "isAtAll": isAtAll
            }
        }

        msg = json.dumps(msg)
        print(msg)
        res = RunMethod().run_main("post",url,msg,headers)

        # 发送link类型的消息
        # title 消息标题
        # content 消息内容
        # messageUrl 点击消息跳转的URL
        # picUrl 图片URL

    def sendLinkTextMsg(self, title, content, messageUrl, picUrl=None):
        msg = {
            "msgtype": "link",
            "link": {
                "text": content,
                "title": title,
                "picUrl": picUrl,
                "messageUrl": messageUrl
            }
        }

        msg = json.dumps(msg)
        res = RunMethod().run_main("post", url, msg, headers)


if __name__ == '__main__':
    SendDingTalk().sendTextMsg("测试消息",['13652376810','18911269591'],True)
    # SendDingTalk().sendLinkTextMsg("测试消息","这是一个超链接消息，点击跳转到百度","https://www.baidu.com")