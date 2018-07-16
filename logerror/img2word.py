# coding:utf-8

import urllib2, sys,base64
import urllib
import ssl
import requests
import json

class Img2word:
    def __init__(self,path):
        self.path=path

    def get_access_token(self):
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Z3gbD8Shb7Gxd19lkmnnKekl&client_secret=c4Rrr94YAdDmGK86xEcRaBv9Sv15Z40H'
        header={
            'Content-Type':'application/json; charset=UTF-8'
        }
        req=requests.get(url=host,headers=header)
        data=json.loads(req.text)
        # print(data['access_token'])
        access_token=data['access_token']
        return access_token

    def get_words(self):
        # access_token = '#####调用鉴权接口获取的token#####'
        access_token=self.get_access_token()
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage?access_token=' + access_token
        # 二进制方式打开图文件
        f = open(self.path, 'rb')
        # 参数image：图像base64编码
        img = base64.b64encode(f.read())
        params = {"url": "http://img2.3lian.com/2014cf/f4/177/d/108.jpg"}
        params = urllib.urlencode(params)
        request = urllib2.Request(url, params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        content = response.read()
        if (content):
            res=json.loads(content)['words_result']
        str=''
        for i in res:
            str=str+i['words']+'\n'
        return str

if __name__=='__main__':
    im=Img2word('E:/python/logerror/code.jpg')
    print(im.get_words())