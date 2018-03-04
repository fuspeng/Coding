import requests
#import json
class Cfda(object):
	# 初始化函数/方法 先执行
	def __init__(self):
		self.url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'

	# 普通方法
	def getCfda(self,data):
		self.html = requests.post(self.url, data = data)
		
		# 提取信息/批量 NO.1
		for m in range(15): #已经知道每页15个
#			print(self.html.json()['list'][m]['EPS_NAME']) # json是一种文件格式
			self.data = self.html.json()['list'][m]['EPS_NAME']
			self.data2File(self.data)
		# # NO.2 函数式 map(f,[4,5,6]), f函数作用于后面的[4,5,6],返回列表
		# self.data = list(map(lambda n:self.html.json()['list'][n]['EPS_NAME'], range(15))) # json是一种文件格式)
		# print(self.data)

	# 定义一个写文件的方法
	def data2File(self, dat):
		with open('file.txt','a',encoding='utf-8') as ff:
			ff.write(dat + '\n')

# 如果在该文件下运行，程序会执行if判断语句下面的内容
# 如果该文件被其他文件导入运行或者调用，if下面的程序不会执行
if __name__ == '__main__':
	# 实例化对象
	cfda = Cfda() # 隐式

	# 准备参数
	data = {
	'applyname':'',
	'applysn':'',
	'conditionType':'1',
	'on':'true',
	'page':2, # 关键参数1
	'pageSize':15, # 关键参数2
	'productName':''
	}


	for i in range(5):
		data['page'] = i
		cfda.getCfda(data)
