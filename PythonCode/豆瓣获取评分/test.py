'''
Title = 获取舌尖上的中国的豆瓣短评
Date = 2018-03-01
'''
# 导入模块
import requests  # pip install requests
import re

# 网址 同意资源定位符
url = 'https://movie.douban.com/subject/25875034/comments?start=40&limit=20&sort=new_score&status=P&percent_type='

index = 0

for m in range(0,100,20):
	url2 = 'https://movie.douban.com/subject/25875034/comments?start={page}&limit=20&sort=new_score&status=P&percent_type='.format(page=m)
	# 打开目录，并获取里面的内容
	html = requests.get(url2)
	# requests.get(url, cookies = cookie)

	#print(html) # 返回200 成功，表示进入那个目录了
	#print(html.text) # 查看一下， 获取到了静态页面内容

	# 筛选， 正则表达式
	data = re.findall('<p class="">(.*?)\n        </p>', html.text, re.S)
	#print(data)
	
	with open(r'E:\PythonProjects\PythonWithSublime\豆瓣获取评分\评分.txt','a',encoding='utf-8') as f1:
		for lineData in data:
			index = index + 1
			f1.write('%02d %s\n'%(index, lineData))

# # 打开目录，并获取里面的内容
# html = requests.get(url)

# #print(html) # 返回200 成功，表示进入那个目录了
# #print(html.text) # 查看一下， 获取到了静态页面内容

# # 筛选， 正则表达式
# data = re.findall('<p class="">(.*?)\n        </p>', html.text, re.S)
# #print(data)

# with open(r'E:\PythonProjects\PythonWithSublime\豆瓣获取评分\评分.txt','w') as f1:
# 	index = 0
# 	for lineData in data:
# 		index = index + 1
# 		f1.write('%02d %s\n'%(index, lineData))
	#f1.write(data[0])

# index = 0
# for li in data:
# 	index = index + 1
# 	print('第%02d条 %s'%(index,li))


# 数据展示 jieba模块 中文分词 import jieba 已安装
# 数据展示 wordcloud 模块 import wordcloud as WordCloud 此项手动安装
# 数据展示 matplotlib.pyplot import matplotlib.pyplot as plt