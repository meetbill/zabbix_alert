#!/usr/bin/python 
#coding=utf8
"""
# Author: Bill
# Created Time : 2016-09-21 17:31:42

# File Name: w.py
# Description:

SMTPS和SMTP协议一样，也是用来发送邮件的，只是更安全些，防止邮件被黑客截取泄露，还可实现邮件发送者抗抵赖功能。防止发送者发送之后删除已发邮件，拒不承认发送过这样一份邮件。

# 默认SMTP端口为25
# 默认SMTPS端口为465

"""
import smtplib 
from email.mime.text import MIMEText 
import os 
import argparse
import logging
import datetime
 
#QQ enterprise
#smtp_server = 'smtp.exmail.qq.com' 
#smtp_port = 25 
#smtp_user = 'xxxxx@qq.com'
#smtp_pass = '*********'
#smtp_tls = False
#smtp_info = "sc:"

#163 Mail
#smtp_server = 'smtp.163.com' 
#smtp_port = 25
#smtp_user = 'alarm@163.com'
#smtp_pass = '*******'
#smtp_tls = False
#smtp_info = "sc:"

#Duomi Mail
#smtp_server = 'mail.duomi.com' 
#smtp_port = 25 
#smtp_user = 'jason.jia@duomi.com'
#smtp_pass = '********'
#smtp_tls = False
#smtp_info = "sc:"

smtp_server = 'smtp.exmail.qq.com' 
smtp_port = 465 
smtp_user = 'xxxxx@qq.com'
smtp_pass = '*********'
smtp_tls = True
# 提示信息
smtp_info = "sc:"

def send_mail(mail_to,subject,content): 
    '''
    mail_to:发给谁
    Subject:主题
    content:内容
    send_mail("XXXXXXXXXXX@qq.com","sub","content")
    '''
    msg = MIMEText(content) 
    msg['Subject'] = smtp_info + subject 
    msg['From'] = smtp_user 
    msg['to'] = mail_to 
    global sendstatus
    global senderr
    if smtp_tls:
        smtp_class = smtplib.SMTP_SSL
    else:
        smtp_class = smtplib.SMTP
     
    try: 
        smtp = smtp_class() 
        smtp.connect(smtp_server,smtp_port) 
        smtp.login(smtp_user,smtp_pass) 
        smtp.sendmail(smtp_user,mail_to,msg.as_string()) 
        smtp.close() 
        print 'send ok'
        sendstatus = True 
    except Exception,e: 
        senderr=str(e)
        print senderr
        sendstatus = False 
     
def logwrite(sendstatus,mail_to,content):
    logpath='/var/log/zabbix/alert'

    if not sendstatus:
        content = senderr

    if not os.path.isdir(logpath):
        os.makedirs(logpath)

    t=datetime.datetime.now()
    daytime=t.strftime('%Y-%m-%d')
    daylogfile=logpath+'/'+str(daytime)+'.log'
    logging.basicConfig(filename=daylogfile,level=logging.DEBUG)
    os.system('chown zabbix.zabbix {0}'.format(daylogfile))
    logging.info('*'*130)
    logging.debug(str(t)+' mail send to {0},content is :\n {1}'.format(mail_to,content))


if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Send mail to user for zabbix alerting')
    parser.add_argument('mail_to',action="store", help='The address of the E-mail that send to user ')
    parser.add_argument('subject',action="store", help='The subject of the E-mail')
    parser.add_argument('content',action="store", help='The content of the E-mail')
    args = parser.parse_args()
    mail_to=args.mail_to
    subject=args.subject
    content=args.content

    send_mail(mail_to,subject,content)
    logwrite(sendstatus,mail_to,content)

    #send_mail("772384788@qq.com","ww" , "hhhhhhhhhhhhh")
    #logwrite(sendstatus,"772384788@qq.com","ww")

