# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"


import sys
sys.path.append("F:/python work/MyDjangos/MyTester")
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


    def sendMarkdownMsg(self,title,text,atMobiles=None,isAtAall=False):
        msg = {
                 "msgtype": "markdown",
                 "markdown": {
                     "title":title,
                     "text": text
                 },
                "at": {
                    "atMobiles": atMobiles,
                    "isAtAll": isAtAall
                }
             }
        msg = json.dumps(msg)
        print(msg)
        res = RunMethod().run_main("post", url, msg, headers)

    def send_dingrobot_main(self,pass_list,fail_list):
        pass_num = len(pass_list)
        fail_num = len(fail_list)
        count_num = pass_num + fail_num

        # 成功率，失败率
        pass_result = '%.2f%%' % (pass_num / count_num * 100)
        fail_result = '%.2f%%' % (fail_num / count_num * 100)

        sub = '接口自动化测试报告'
        content = '**此次一共运行接口%s个，通过%s个，失败%s个，通过率%s，失败率%s**' % (count_num, pass_num, fail_num, pass_result, fail_result)

        self.sendMarkdownMsg(sub, content)



if __name__ == '__main__':
    SendDingTalk().sendTextMsg("测试消息",['13652376810','18911269591'],True)
    SendDingTalk().send_dingrobot_main([1,2,3],[4,5])
    # SendDingTalk().sendLinkTextMsg("测试消息","这是一个超链接消息，点击跳转到百度","https://www.baidu.com")
