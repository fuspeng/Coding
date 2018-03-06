# !/usr/bin/env python
# -*- coding:utf-8 -*-

from tornado import web, ioloop,httpserver
from create_qr_code import get_code_by_str

# 文件句柄
# 全局变量
SIGN_FILE_HANDLER = open('sign.csv','a')
# 写上表头
SIGN_FILE_HANDLER.write('%s,%s,%s\n'%('姓名','工号','部门'))


class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        # self.write('未来的python大牛们')
        self.render('index.html')

# 签到模块
class SignHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('sign.html')
    def post(self, *args, **kwargs):
        name = self.get_argument("name")
        number = self.get_argument("number")
        department = self.get_argument("department")
        print(name,number,department)
        # 将受到的数据写入csv文件
        SIGN_FILE_HANDLER.write('%s,%s,%s\n'%(name,number,department))
        SIGN_FILE_HANDLER.flush()

# 生成二维码
class CodeHandler(web.RequestHandler):
    def get(self,*args, **kwargs):
        # 生成一个二维码图片，根据下方传递的地址
        code_img_handler = get_code_by_str('http://image.baidu.com')
        self.write(code_img_handler.getvalue())


# 路由
application = web.Application([
    (r"/sign", SignHandler),
    (r"/login", MainPageHandler),
    (r"/code", CodeHandler)
])

# 浏览器输入localhost/login 得到百度图片的网址二维码
# 浏览器输入localhost/sign 进入签到页面，可在本地保存成csv文件
if __name__ == "__main__":
    http_server = httpserver.HTTPServer(application)
    http_server.listen(80)
    ioloop.IOLoop.current().start()