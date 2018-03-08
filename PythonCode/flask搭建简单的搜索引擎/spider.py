import requests

# 模拟浏览器，百度有反爬措施
userAgent={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}

# 根据keyword关键字，通过百度api搜索并返回结果
def getBdMsg(keyword):
    res = requests.get('https://www.baidu.com/s?wd={}'.format(keyword),headers=userAgent)
    # 返回结果将百度的返回首页logo替换成本地图片
    return res.text.replace('//www.baidu.com/img/baidu_jgylogo3.gif','static/images/python.jpg')

if __name__ == '__main__':
    print(getBdMsg('python'))