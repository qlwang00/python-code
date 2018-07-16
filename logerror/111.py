# coding:utf-8

import requests

url='https://aip.baidubce.com/rest/2.0/ocr/v1/webimage?access_token=24.17352672217e2cdf0efd7516ee47769d.2592000.1533971223.282335-11522102'

params = {"url":"http://img2.3lian.com/2014cf/f4/177/d/108.jpg"}
header={'Content-Type':'application/x-www-form-urlencoded'}
res=requests.post(url=url,params=params,headers=header)

print(res.content)

