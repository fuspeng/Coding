# 使用matplotlib绘制饼图
import numpy as np
import matplotlib.pyplot as plt
import math
import random

# 设置全局字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决'-'表现为方块的问题
plt.rcParams['axes.unicode_minus'] = False

def pie(data, img_name):
    # data = {
    # '南京':(60, '#7199cf'),
    # '上海':(45, '#4fc4aa'),
    # }
    # 设置绘图对象的大小
    fig = plt.figure(figsize=(8, 8))

    cities = data.keys()
    values = [x for x in data.values()]
    print(values)
    # colors = [x[1]] for x in data.values()]

    ax1 = fig.add_subplot(111)
    ax1.set_title(img_name)

    labels = ['{}:{}'.format(city, value) for city, value in zip(cities, values)]

    # 设置饼图的突出显示
    explode = [0, 0.1]

    # 画饼状图，并且指定对应的标签和颜色
    # 指定阴影效果
    ax1.pie(values, labels=labels, explode = explode, shadow = True)
    plt.savefig(img_name.format('.jpg'))
    plt.show()


def bar(data, img_name):
    #values = [x for x in data.values()]

    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # jet = cm = plt.get_cmap('jet')
    # cNorm  = colors.Normalize(vmin=0, vmax=values[-1])
    # scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
    dataY = [x for x in data.values()]
    dataX = [x for x in data.keys()]

    curves = [format_color() for i in range(len(data))]
    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(111)
    ax1.set_title(img_name)

    ax1.bar(range(len(dataY)), dataY, tick_label=dataX, color=curves)
    plt.savefig(img_name.format('.jpg'))
    plt.show()

def format_color():
    colorR = ''
    for i in range(6):
        strNum = math.floor(random.uniform(0,17))
        colorf = hex(strNum)[-1]
        colorR = colorR + colorf
    colorR = '#' + colorR
    return colorR