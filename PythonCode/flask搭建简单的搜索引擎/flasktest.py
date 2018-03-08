from flask import Flask
from flask import request
from flask import render_template
#import urllib
# 导入自己写的方法
from spider import getBdMsg

app = Flask(__name__)

# 装饰器，给函数增加新功能
@app.route('/')
def index():
    return render_template('index.html')

# 接受提交表单的行为，要加上methods,前端提交时传递/s
@app.route('/s')
def abc():
    keyword = request.args.get('keyword')	# 从名称为wd的input中获取输入的关键字
    text = getBdMsg(keyword)				# 根据关键字搜索百度，并返回结果
    return text

if __name__ == '__main__':
    app.run()