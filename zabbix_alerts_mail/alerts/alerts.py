#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Zabbix SMTP Alert script
"""
import sys
import smtplib
from email.mime.text import MIMEText


#邮件发送列表，发给哪些人
#mailto_list=["XXXXX@gmail"]
#设置服务器，用户名、口令以及邮箱的后缀
mail_host="smtp.163.com"
mail_user="XXXXX"
mail_pass="XXXXX"
mail_postfix="163.com"

#定义send_mail函数
def send_mail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("XXXXXXXXXXX@qq.com","sub","content")
    '''
    address=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = address
    msg['To'] =to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(address, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
       send_mail(sys.argv[1], sys.argv[2], sys.argv[3])
       #send_mail("XXXXXXXXX@qq.com","ww" , "hh")

