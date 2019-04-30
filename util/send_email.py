# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

import smtplib
from email.mime.text import MIMEText




class SendEmail:
    global send_user
    global password
    global email_host
    send_user = 'ebmlc@ebmsz.com'
    password = 'Licheng123'
    email_host = 'smtp.exmail.qq.com'


    # 发送邮件
    # user_list 收件人
    # sub 邮件主题
    # content 邮件内容
    def send_mail(self,user_list,sub,content):
        user = 'Tester'+'<'+send_user+'>'
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)

        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

    def send_mail_main(self,pass_list,fail_list):
        pass_num = len(pass_list)
        fail_num = len(fail_list)
        count_num = pass_num+fail_num

        # 成功率，失败率
        pass_result = '%.2f%%' %(pass_num/count_num*100)
        fail_result = '%.2f%%' %(fail_num/count_num*100)

        user_list = ['yoyosee@dingtalk.com']
        sub = '接口自动化测试报告'
        content = '此次一共运行接口%s个，通过%s个，失败%s个，通过率%s,失败率%s' %(count_num,pass_num,fail_num,pass_result,fail_result)

        self.send_mail(user_list,sub,content)


if __name__ == '__main__':
    sendmail = SendEmail()
    # user_list = ['yoyosee@dingtalk.com']
    # sub = '这是个测试邮件'
    # content = '这就是个测试邮件'
    # sendmail.send_mail(user_list,sub,content)
    sendmail.send_mail_main([1,2,3],[4,5])

