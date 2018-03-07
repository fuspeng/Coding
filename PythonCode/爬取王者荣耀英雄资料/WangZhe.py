'''
作用：
	下载王者荣耀官网英雄壁纸
时间：
	2018-03-07
'''
# 导入模块
import requests # pip install requests
import json
import time
import urllib
import os

# 读取英雄json文件信息，关键是数字名称
with open(r'herolist.json','r',encoding='utf-8') as f:
	jsonFile = json.load(f)

# 批量提取数据
for m in range(5):#len(jsonFile)):
	time.sleep(0.05)
	eName 		= jsonFile[m]['ename'] # 英雄编号
	cName 		= jsonFile[m]['cname'] # 英雄中文名称
	skinName 	= jsonFile[m]['skin_name'].split('|') # 皮肤名称
	
	# 获取皮肤数量,用|切割
	skinCount = len(skinName)

	# 构造皮肤地址并下载
	for n in range(1, skinCount + 1):
		pictureUrl = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/%s/%s-bigskin-%d.jpg'%(eName,eName,n)

		# 图片路径+名称 ，在当前路径下为每个英雄生成对应文件夹,王者荣耀英雄壁纸\\英雄名
		path = '王者荣耀英雄壁纸\\%s'%(cName)

		# 创建英雄名称命名的文件夹，为防止重复创建，先判断是否存在
		if not os.path.exists(path):
			os.makedirs(path)
		else:
			print(path,'已存在')

		# 文件路径+皮肤名称
		pictureFileName = '%s\\%s.jpg'%(path,skinName[n-1])
	
		# 下载图片
		# request.get(pictureUrl) # 方法一
		
		# content 代表是以二进制格式表示
		picture = requests.request('get',pictureUrl).content # 方法二
		
		# # 保存图片，图片都是二进制
		# with open(pictureFileName,'ab') as fSkin:
		# 	fSkin.write(picture)
	
		# 方法二,用urllib.request.urlretrieve直接下载到本地
		urllib.request.urlretrieve(pictureUrl,pictureFileName)
