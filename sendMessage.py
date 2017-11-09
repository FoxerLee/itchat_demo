# -*- coding:utf-8 -*-
import itchat
import requests
import sys

# 转变编码格式 不然可能报错
reload(sys)
sys.setdefaultencoding('utf-8')

key = '0e5bb6fec1fe4f609d60714336ea6fba'

def get_response(msg):

    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': key,
        'info': msg,
        'userid': 'wechat-robot',
    }

    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常

        text = r.get('text')

        print text
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 没收到图灵机器人的话，将会回复一个假的消息
    default_reply = '我是一个假的消息'
    # 从图灵机器人得到的消息
    reply = get_response(msg['Text'])
    reply.encode('utf8')
    print reply

    return reply or default_reply

# 登录
itchat.auto_login(hotReload=True)
itchat.run()
