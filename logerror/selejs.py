# coding:utf-8

from selenium import webdriver
import requests
import time
from PIL import Image
from img2word import Img2word

dv=webdriver.PhantomJS('D:/phantomjs-2.1.1-windows/bin/phantomjs.exe')

url='http://123123g.com:8080/KLH/web'
dv.get(url)

dv.find_element_by_id('loginName').send_keys('G6847')
dv.find_element_by_id('passWord').send_keys('119722')
s=dv.find_element_by_id('Verify_codeImag').get_attribute('src')

# 下载图片
# req=requests.get(s,stream=True)
# img=req.content
# try:
#     with open("code.jpg" ,"wb") as f:
#         f.write(img)
# except IOError:
#     print("IO Error\n")
# finally:
#     f.close
# # 识别验证码
# path='code.jpg'
# im=Img2word(path)
# code=im.get_words()
# print(code)

dv.save_screenshot('login.jpg')
# 显示验证码图片
img=Image.open('login.jpg')
img.show()
# 手动输入验证码
customerCode=input()

dv.find_element_by_id('customerCode').send_keys(customerCode)
dv.find_element_by_id('login_button').click()
time.sleep(5)

items=dv.find_elements_by_xpath('//*[@id="fstyleInfo"]/dd')
for i in items:
    print(i.text)

dv.find_element_by_xpath('//*[@id="fstyleInfo"]/dd[4]').click()
time.sleep(5)
items=dv.find_elements_by_xpath('//*[@id="goods"]/li')
for item in items:
    name=item.find_element_by_xpath('span[3]').text
    print(name)

dv.quit()
