# !/usr/bin python
# -*- coding:utf-8 -*-

# 导入模块
import urllib
import requests
import time

# 模拟浏览器登陆的header
# !!!!!!请从你的浏览器中拷贝过来!!!!!!
# !!!!!!请从你的浏览器中拷贝过来!!!!!!
# !!!!!!请从你的浏览器中拷贝过来!!!!!!
header = {
'accept':'application/json, text/javascript, */*; q=0.01',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9',
'cookie':'tt_webid=6532408595795297806; uuid="w:b8e3e7bc92f6465990aaec85cfba16a9"; _ga=GA1.2.855543767.1520944902; _gid=GA1.2.1124724095.1520944902; csrftoken=3dab60a193bf0db413c0be5cd5f167a9; _gat=1',
'referer':'https://www.neihanshequ.com/',
'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'x-csrftoken':'3dab60a193bf0db413c0be5cd5f167a9',
'x-requested-with':'XMLHttpRequest',
}
# !!!!!!请从你的浏览器中拷贝过来!!!!!!

# 用Chrome解析后发现真实的json地址如下
urlActual = 'https://www.neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1520946090.0'

# 利用时间戳可以获取到下一页的max_time
html =requests.get(urlActual,headers=header)
max_time = html.json()['data']['max_time']

while isinstance(max_time,int) or isinstance(max_time, float):
    time.sleep(3)
    # 获取网页源码，就是json文件
    html = requests.get(urlActual,headers=header)
    # 转为json格式文件
    data = html.json()

    with open('result.txt', 'a',encoding='utf-8') as f:
        for n in range(len(data['data']['data'])):
            dataWrite = data['data']['data'][n]['group']['content']
            f.write(dataWrite+"\n-----\n")
    max_time = data['data']['max_time']
    print(max_time)
    urlActual = "https://www.neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time={}".format(max_time)


