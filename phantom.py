# coding:utf-8

from selenium import webdriver
import time

def login():
    dv.get("http://b2b.frxs.com")
    account = '00020109'
    pwd = '134827'

    dv.find_element_by_id('UserAccount').send_keys(account)
    dv.find_element_by_id('Password').send_keys(pwd)
    dv.find_element_by_id('btnLogin').click()
    time.sleep(5) # 登录完成 加载页面

def get_data(): # 获取数据
    data_item = dv.find_elements_by_xpath('//*[@id="colume"]/ol/li')
    for i in data_item:
        name = i.find_element_by_xpath('h1/a|h1').text
        print(name)

if __name__=='__main__':
    dv = webdriver.PhantomJS('D:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    login()

    category_items=dv.find_elements_by_xpath('//*[@id="index"]/div[1]/ul/li')
    category_urls=[]
    for i in category_items: # 获取分类链接
        url=i.find_element_by_xpath('i/a').get_attribute('href')
        if url is not None:
            category_urls.append(url)

    for j in category_urls: # 获取每个分类链接下的商品数据
        dv.get(j)
        # 获取首页商品数据
        print(j)
        get_data()
        next_page=dv.find_element_by_link_text('下一页 >').get_attribute('href')
        # 下一页获取
        while next_page is not None:
            print(next_page)
            dv.find_element_by_link_text('下一页 >').click()
            get_data()
            next_page = dv.find_element_by_link_text('下一页 >').get_attribute('href')

    dv.quit()
