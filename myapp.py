# coding: utf-8

import time
import MySQLdb
from flask import Flask, g, request, make_response, render_template
import hashlib
import xml.etree.ElementTree as ET

app = Flask(__name__)
app.debug = True

APP_ID = 'wxd44103007c818b7b'
APP_SECRET = 'd4624c36b6795d1d99dcf0547af5443d'
TOKEN = 'ChildhoodAndy'
TIPS = "tip test"

GET_ACCESS_TOKE_URL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}'

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        token = TOKEN
        query = request.args
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr', '')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        if (hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)

    xml_recv = ET.fromstring(request.data)
    ToUserName = xml_recv.find('ToUserName').text
    FromUserName = xml_recv.find('FromUserName').text
    Content = xml_recv.find('Content').text
    reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"

    if Content == 'sgss':
        Content = '骚哥就是帅气的磊哥，我的好大哥'
    elif Content == 'ty':
        Content = '田野是大兵的好同事，他非常喜欢跑步，正能量爆表的一个爷们'
    response = make_response( reply % (FromUserName, ToUserName, str(int(time.time())), Content))
    response.content_type = 'application/xml'
    return response

    return "Hello, world! - Flask comes from Beijing."


#--------------------------bind phone-------------------------------------------------
@app.route('/bindphone', methods = ['GET', 'POST'])
def bind_phone():
    if request.method == 'GET':
        return render_template('bindphone.html')
    else:
        
