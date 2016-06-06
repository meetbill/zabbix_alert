#!/usr/bin/python
#coding=utf8
"""
# Author: Bill
# Created Time : 2016-06-06 22:23:33

# File Name: weixin.py
# Description:

"""
import urllib2
import json
import sys
import time
import os
import shutil
import logging

def gettoken(corp_id,corp_secret):
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corp_id + '&corpsecret=' + corp_secret
    try:
        token_file = urllib2.urlopen(gettoken_url)
    except urllib2.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token

def senddata(access_token,user,content):
    try:
        send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
        send_values = {
            u"touser":user,
            u"msgtype":"text",
            u"agentid":"2",
            u"text":{
                u"content":content
                },
            u"safe":"0"
            }
        #send_data = json.dumps(send_values, ensure_ascii=False).encode(encoding='UTF8')
        send_data = json.dumps(send_values, ensure_ascii=False)
        send_request = urllib2.Request(send_url, send_data)
        response = urllib2.urlopen(send_request)
        msg = response.read()
        print("returned value : " + str(msg))
    except:
        msg="###"
        print("returned value : " + str(msg))

if __name__ == "__main__":
    default_encoding = 'utf-8'
    if sys.getdefaultencoding() != default_encoding:
        reload(sys)
        sys.setdefaultencoding(default_encoding)
    user = str(sys.argv[1])
    title = str(sys.argv[2])
    content = str(sys.argv[3])
    corpid = ''
    corpsecret = ''
    accesstoken = gettoken(corpid,corpsecret)
    senddata(accesstoken,user,content)
