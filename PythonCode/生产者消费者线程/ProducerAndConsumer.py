'''
场景
生产者：呀，产品<1000了，生产100个，抽根烟；
消费者：呀，产品>100个，买它3个。
消费者：呀，还>100个，再买它3个。
消费者：买买买~~~
突然，生产者发现产品<1000了。掐掉烟头，生产100个。
'''
# 导包
import threading
import time

__author__ = '符灏'

# 我要创建一个生产者线程
class Producer(threading.Thread):
    # 继承方式创建线程是，要重写run方法
    def run(self):
        # 告诉我们的Python解释器，我要对全局变量进行修改了
        global count
        # 这个死循环就是用来模拟市场上的交易行为
        while True:
            # 判断生产者是否获得了锁
            if con.acquire():
                # 生产者的产品数量是否足够
                if count > 1000:
                    # 当生产者生产了足够多的产品是，便让生产者进入阻塞状态
                    con.wait()
                else:
                    count = count + 100
                    print(self.name,'-生产者-当前市场上的产品数:', count)
                    # 通知消费者消费产品
                    con.notify()
                con.release()
            time.sleep(1)

# 我要创建一个消费者线程
class Consumer(threading.Thread):
    def run(self):
        global count
        while True:
            if con.acquire():
                if count < 100:
                    # 市场上的产品小于100，停止购买
                    con.wait()
                else:
                    count -= 3
                    print(self.name,'-消费者-当前市场上的产品数:', count)
                    con.notify()
                con.release()
            time.sleep(1)

# 写函数入口
if __name__ == '__main__':
    # 定义初始商品数量
    count = 500
    # 创建我们的条件变量
    con = threading.Condition()

    # 创建3个生产者
    for i in range(3):
        p = Producer()
        p.start()

    # 创建5个消费者
    for i in range(5):
        c = Consumer()
        c.start()