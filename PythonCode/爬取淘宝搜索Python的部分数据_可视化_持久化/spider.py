# ------------ 爬取淘宝搜索python的部分信息 -----------
# 网络爬虫
# -浏览模拟器
# -批量爬取我们需要的网络资源

# Step1.导入模块
import requests
import re
import json
import time
import draw
import xlwt

# 数据
DATA = []


# 发送请求的两种方式： 1.get 2.post
url = 'https://s.taobao.com/search?q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180302&ie=utf8'

# 下载数据
response = requests.get(url)
html = response.text

# 处理数据
content = re.findall(r'g_page_config = (.*?)g_srp_loadCss', html, re.S)[0].strip()

# 格式化数据
content = content[:-1]
content = json.loads(content)

data_list = content['mods']['itemlist']['data']['auctions']
#print(data_list)

for item in data_list:
    temp = {
        'title':item['title'],
        'view_price':item['view_price'],
        'view_sales':item['view_sales'],
        'view_fee':'否' if float(item['view_fee']) else '是',
        'isTmall':'是' if item['shopcard']['isTmall'] else '否',
        'area':item['item_loc'],
        'name':item['nick'],
        'detail_url':item['detail_url'],

    }
    DATA.append(temp)


url2 = 'https://s.taobao.com/api?_ksTS=1519997224531_224&callback=jsonp225&ajax=true&m=customized&stats_click=search_radio_all:1&q=python&s=36&imgfile=&initiative_id=staobaoz_20180302&bcoffset=0&js=1&ie=utf8&rn=2575a378b35e7b593e3bae6bd75443e7'
response2 = requests.get(url2)
html2 = response2.text
data_list = json.loads(re.findall(r'{.*}', html2)[0])['API.CustomizedApi']['itemlist']['auctions']
for item in data_list:
    temp = {
        'title':item['title'],
        'view_price':item['view_price'],
        'view_sales':item['view_sales'],
        'view_fee':'否' if float(item['view_fee']) else '是',
        'isTmall':'是' if item['shopcard']['isTmall'] else '否',
        'area':item['item_loc'],
        'name':item['nick'],
        'detail_url':item['detail_url'],
    }
    DATA.append(temp)

# 翻页
for i in range(1, 10):
    data_value = 44*i
    t = time.time() # 时间戳
    ksTs = "%s_%s" % (int(t*1000), str(t)[-3:])
    callback = "jsonp%s" % (int(str(t)[-3:])+1)
    url = 'https://s.taobao.com/search?data-key=s&data-value={}&ajax=true&_ksTS={}&callback={}&q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180302&ie=utf8&bcoffset=4&ntoffset=0&p4ppushleft=1%2C48'.format(data_value, ksTs, callback)
    r3 = requests.get(url)
    html = r3.text
    data_list = json.loads(re.findall(r'{.*}', html)[0])['mods']['itemlist']['data']['auctions']
    #提取数据
    for item in data_list:
        temp = {
            'title':item['title'],
            'view_price':item['view_price'],
            'view_sales':item['view_sales'],
            'view_fee':'否' if float(item['view_fee']) else '是',
            'isTmall':'是' if item['shopcard']['isTmall'] else '否',
            'area':item['item_loc'],
            'name':item['nick'],
            'detail_url':item['detail_url'],
        }
        DATA.append(temp)

# print(len(DATA))

# 分析画图
# 1 包邮和不包邮的比例
data1 = {'包邮':0, '不包邮':0}

# 2 天猫和淘宝的比例
data2 = {'天猫':0, '淘宝':0}

# 3 地区分布
data3 = {}

for item in DATA:
    if item['view_fee'] == '否':
        data1['不包邮'] += 1
    else:
        data1['包邮'] += 1
    if item['isTmall'] == '是':
        data2['天猫'] += 1
    else:
        data2['淘宝'] += 1
    data3[item['area'].split(' ')[0]] = data3.get(item['area'].split(' ')[0],0) + 1
print(data1)
print(data2)
print(data3)

draw.pie(data1,'是否包邮')
draw.pie(data2, '是否天猫')
draw.bar(data3, '地区分布')

# 持久化
f = xlwt.Workbook(encoding='utf-8')
sheet01 = f.add_sheet('sheet1', cell_overwrite_ok = True)
# 写标题
sheet01.write(0, 0, '标题')
sheet01.write(0, 1, '标价')
sheet01.write(0, 2, '购买人数')
sheet01.write(0, 3, '是否包邮')
sheet01.write(0, 4, '是否天猫')
sheet01.write(0, 5, '地区')
sheet01.write(0, 6, '点名')
sheet01.write(0, 0, 'url')

# 写内容
mark = ('title','view_price', 'view_sales', 'view_fee', 'isTmall', 'area', 'name', 'detail_url')
for i in range(len(DATA)):
    for j in range(0,8):
        sheet01.write(i+1, j, DATA[i][mark[j]])

f.save('淘宝搜索Python的结果.xls')