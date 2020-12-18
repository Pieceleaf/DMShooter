# coding=utf-8
import json
import re
import requests, time, random

class Sender:
    bvid = ''
    cid = ''
    msg = ''
    videotim = ''
    headers = {
        'authority': 'api.bilibili.com',
        'accept': '*/*',
        'dnt': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.27 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.bilibili.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.bilibili.com/',
        'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
        'cookie': '',
    }

    data = {
        'type': '1',
        'oid': '261793445',
        # mode7的msg格式依次为{"x0", "y0", "alpha0-alpha1", "duration", "文字", "rotateZ", "rotateY", "x1", "y1", "运动耗时", "运动延迟时间(ms)", "0/1（文字描边）", "字体", "0/1（线性加速）"}
        'msg': '[0.3,0.4,"0.7-1",5,"弹幕测试",0,0,0.5,0.2,2000,0,0,"仿宋",1]',
        'progress': '0',
        'color': '16777215',
        'fontsize': '36',
        'pool': '0',
        'mode': '7',
        'rnd': str(int(round(time.time()) * 1000000 + random.randint(0, 999999))),
        'plat': '1',
        'bvid': 'BV1hp411f7me',
        'csrf': ''
    }

    def __init__(self, bvid, cid, cookie):
        self.data['bvid'] = bvid
        self.data['oid'] = cid
        pattenStr = r"bili_jct=(\w+)"
        patten = re.compile(pattenStr)
        bili_jct = patten.findall(cookie)[0]
        #SESSDATA = idList[0]
        self.headers['cookie']=cookie
        self.data['csrf'] = bili_jct


    def sendMod1(self, msg, videotim):
        self.data['msg'] = msg
        self.data['progress'] = videotim
        self.data['mode'] = '1'
        self.data['fontsize'] = '25'
        self.data['color'] = '16777215'
        response = requests.post('https://api.bilibili.com/x/v2/dm/post', headers=self.headers, data=self.data)
        print(self.data)

        return response.text

    pass

    def sendMod7(self, msg, videotim,fontsize,color):
        self.data['msg'] = msg
        self.data['progress'] = videotim
        self.data['fontsize'] = fontsize
        self.data['color'] = color
        self.data['mode'] = '7'
        self.data['rnd'] = str(int(round(time.time()) * 1000000 + random.randint(0, 999999)))
        response = requests.post('https://api.bilibili.com/x/v2/dm/post', headers=self.headers, data=self.data)
        print(r"Send: "+json.dumps(self.data).encode('utf-8').decode('unicode_escape'))
        return response

    pass

    def send(self):
        videotim = '0'
        msg = '弹幕 PYTHON TEST'
        self.data['msg'] = msg.encode('unicode_escape')
        self.data['progress'] = videotim
        response = requests.post('https://api.bilibili.com/x/v2/dm/post', headers=self.headers, data=self.data)
        print(self.data)

        return response

    pass

pass
